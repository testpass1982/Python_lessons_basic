import hw05_easy
import os
import sys

# print ('sys.argv', sys.argv)
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def print_help(param=None):
    print("help - получение справки:")
    print("1. goto <dir_name> - перейти в папку")
    print("2. show - просмотреть содержимое папки")
    print("3. del <dir_name> - удалить папку с именем")
    print("4. mkdir <dir_name> - создание папки")
    print("5. ping - тестовый ключ")

def ping(param=None):
    print("pong")

do = {
    "help": print_help,
    "goto": hw05_easy.goto,
    "show": hw05_easy.print_folders_in_cwd,
    "del": hw05_easy.remove_folder,
    "mkdir": hw05_easy.create_folder,
    "ping": ping
}

try:
    param = sys.argv[2]
except IndexError:
    param = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key](param)
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
