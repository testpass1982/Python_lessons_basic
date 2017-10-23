import logging
import tkinter as tk
from grab import Grab
import re
import urllib.request
import gzip
import os
import sqlite3
from sqlite3 import Error
import json
from datetime import date

""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.g = Grab()
        logging.basicConfig(level=logging.DEBUG)
        if self.get_api_key():
            self.api_key = self.get_api_key()
        else:
            self.api_key = 'No key'
        self.createWidgets()
        if not os.path.isfile('weatherapp.db'):
            self.db_connect()
        self.country_list = []
        self.country_selected = ''
        self.chosen_city = ''
        self.chosen_city_id = ''
        self.temp = 0
        self.date = date.today().isoformat()
        self.weather_id = ''

    def createWidgets(self):
        if len(self.api_key) < 32:
            self.label = tk.Label(self, text="""This is my weather app.
Push button \'Get App_id\' below to register our app
on OpenWeatherMap web-service""")
        else:
            self.label = tk.Label(self, text="""This is my weather app.
We are ready to work with OpenWeatherMap web-service""")
        self.label.pack()
        self.api_label = tk.Label(self, text='API key: ' + self.api_key)
        self.api_label.pack()
        self.quitButton = tk.Button(self, text='Quit', command=lambda: self.quit())
        if len(self.api_key) < 32:
            self.getappid_button = tk.Button(self, text='Get API key', command=lambda: self.getappid())
            self.getappid_button.pack()
        self.get_cities_list_button = tk.Button(self, text='Get cities list', command=lambda: self.get_cities_list())
        self.get_cities_list_button.pack()
        self.show_cities_list_button = tk.Button(self, text='Show weather in cities',
                                                 command=lambda: self.cities_child_window())
        self.show_cities_list_button.pack()
        self.quitButton.pack()

    def cities_child_window(self):
        t = tk.Toplevel(self)
        t.wm_title("Weather in cities")
        l = tk.Label(t, text='Please, choose a country to show weather in it')
        l.pack(side="top", fill="both", expand=True)  # padx=100, pady=10
        listbox = tk.Listbox(t)
        listbox.pack(side='left')
        show_cities_button = tk.Button(t, text='Show cities', command=lambda: _sel_city())
        show_cities_button.pack()

        with open('cities.json', 'r', encoding='UTF-8') as c:
            cities_json = c.read()
            cities_data_decoded = json.JSONDecoder().decode(cities_json)
            country_list = []
            for i in cities_data_decoded:
                if i['country'] not in country_list:
                    country_list.append(i['country'])
            sorted_country_list = sorted(country_list)
            for i in sorted_country_list:
                listbox.insert(tk.END, i)

        self.country_list = country_list

        def _sel_city():
            self.country_selected = sorted_country_list[listbox.curselection()[0]]
            self.show_cities_in_country()

    def show_cities_in_country(self):
        t = tk.Toplevel(self)
        t.wm_title("Choose a city")
        l = tk.Label(t, text='Please choose a city to show weather in it')
        l.pack(side="top", fill="both", expand=True)
        listbox_cities = tk.Listbox(t)
        listbox_cities.pack(side='left')
        show_weather_in_city_button = tk.Button(t, text='Show weather in city', command=lambda: choose_city())
        show_weather_in_city_button.pack()

        with open('cities.json', 'r', encoding='UTF-8') as c:
            cities = []
            city_ids = []
            cities_json = c.read()
            cities_data_decoded = json.JSONDecoder().decode(cities_json)
            for i in cities_data_decoded:
                if self.country_selected == i['country']:
                    listbox_cities.insert(tk.END, i['name'])
                    cities.append(i['name'])
                    city_ids.append(i['id'])

        def choose_city():
            self.chosen_city = cities[listbox_cities.curselection()[0]]
            self.chosen_city_id = city_ids[listbox_cities.curselection()[0]]
            self.show_weather()
            self.weather_window()
            self.write_to_db(self.chosen_city_id, self.chosen_city, self.date, self.temp, self.weather_id)

    def weather_window(self):
        t = tk.Toplevel(self)
        weather_string = 'The  temp in {} is {} now (on {})'.format(self.chosen_city, self.temp, self.date)
        weather_label = tk.Label(t, text=weather_string)
        if self.chosen_city_id != '':
            weather_label.pack(expand=True, padx=100, pady=100)

    def show_weather(self):
        # Для получения температуры по Цельсию:
        # http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a
        link = 'http://api.openweathermap.org/data/2.5/weather'
        id_link = '?id={}&units=metric&appid={}'.format(self.chosen_city_id, self.api_key)
        url = link + id_link
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            self.temp = data['main']['temp']
            self.weather_id = data['weather'][0]['id']

    def getappid(self):
        if not self.get_api_key():
            self.g.go('https://home.openweathermap.org/users/sign_in')
            self.g.doc.set_input('user[email]', 'popov.anatoly@gmail.com')
            self.g.doc.set_input('user[password]', '20111982')
            self.g.doc.submit()
            self.g.go('https://home.openweathermap.org/api_keys')
            self.api_key = self.g.doc.rex_search(re.compile('<td>\s<pre>(.+?)</pre>\s</td>')).group(1)
            with open('app.id', 'r+', encoding='UTF-8') as f:
                while f:
                    if self.api_key in f.readlines():
                        print('it is here')
                        break
                    else:
                        f.write('\n' + self.api_key)
                        print('api key written')
                        break
        else:
            print('we already have api_key')
        self.refresh_root_frame()

    def get_api_key(self):
        with open('app.id', 'r') as f:
            for line in f:
                if len(line) == 32:
                    api_key = line
                    return api_key

    def get_cities_list(self):
        url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
        file_name = url.split('/')[-1]
        u = urllib.request.urlopen(url)
        if not os.path.isfile(file_name):
            with u as response, open(file_name, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
            print('cities downloaded')
        else:
            print('cities already here')

        if not os.path.isfile('cities.json'):
            with open('cities.json', 'wb') as cities:
                with gzip.open(file_name, 'rb') as zipped_cities:
                    cities.write(zipped_cities.read())
                    print('cities unzipped')

    def db_connect(self):
        """== Сохранение данных в локальную БД ==
        Программа должна позволять:
        1. Создавать файл базы данных SQLite со следующей структурой данных
        (если файла базы данных не существует):

        Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных"""
        try:
            conn = sqlite3.connect('weatherapp.db')
            print(sqlite3.version)
            c = conn.cursor()

            c.execute("""CREATE TABLE cities
                    (id integer PRIMARY KEY,
                    city text NOT NULL,
                    date DATE NOT NULL,
                    temperature integer,
                    weather_id integer);""")
            conn.commit()
            conn.close()
        except Error as e:
            print(e)
        finally:
            conn.close()

    def write_to_db(self, city_id, city_name, date, temp, weather_id):
        try:
            conn = sqlite3.connect('weatherapp.db')
            c = conn.cursor()
            # INSERT INTO cities VALUES (3039676, "Parròquia d'Ordino", '2017-10-23', 11.86, 800)
            query = 'INSERT INTO cities VALUES({},"{}","{}",{},{})'.format(city_id, city_name, date, temp, weather_id)
            c.execute(query)
            conn.commit()
            conn.close()
            print('successfully written to database')
        except Error as e:
            print(e)
        finally:
            conn.close()

    def refresh_root_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.createWidgets()


app = Application()
app.master.title('Weather application')
app.mainloop()
