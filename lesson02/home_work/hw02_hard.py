from string import digits

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
eq_arr = equation.split(" ")
x = 2.5
k = -int(''.join(c for c in eq_arr[2] if c in digits))
b = float(eq_arr[-1])
y = k * x + b
print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date0 = '01.11.1985'

# Примеры некорректных дат
date1 = '01.22.1001'
date2 = '1.12.1001'
date3 = '-2.10.3001'

days_in_months = {
    "01": 31,
    "02": 30,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31
}


def date_is_correct(date_str):
    result = []
    d_arr = date_str.split(".")
    # check date:
    try:
        if int(d_arr[0]) in range(1, days_in_months[d_arr[1]] + 1):
            result.append('Дата введена корректно')
        else:
            result.append('Дата введена не корректно')
    except KeyError:
        result.append('Нет такого месяца в календаре')
    # check month:
    if d_arr[1] in days_in_months:
        result.append('месяц введен корректно')
    else:
        result.append('месяц введен не корректно')
    # check year:
    if int(d_arr[2]) in range(1, 9999):
        result.append('год введен корректно')
    else:
        result.append('год введен не корректно')
    result = 'Результат проверки: \n' + ', '.join(result)
    return result


print(date_is_correct('01.22.1001'))

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

N = 13

kom = 1
group = 1
last_in_prev_group = 0
counter = 0
room_on_floor = 0
result_floor = 0
floor_counter = 1
rooms = []
group_counter = 0

# определяем номер группы и последний номер в предудыщей группе
# for kom in range (1, N):
#     if kom - last_in_prev_group == group**2:
#         group+=1
#         last_in_prev_group = kom

while kom < N:
    if kom - last_in_prev_group == group ** 2:
        group += 1
        last_in_prev_group = kom
    kom += 1

# считаем в блоке порядковые номера и этажи
while counter < N - last_in_prev_group:

    last_floor_in_prev_bloc = sum(range(1, group))
    result_floor = last_floor_in_prev_bloc + floor_counter
    counter += 1

    # счетчик этажей в блоке
    if counter % group == 0:
        floor_counter += 1

    # порядковые номера комнат на этаже
    if counter > group:
        room_on_floor = counter % group
    if counter < group:
        room_on_floor = counter
    if counter % group == 0:
        room_on_floor = group

print('этаж', result_floor)
print("счет слева на этаже:", room_on_floor)
