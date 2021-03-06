
__author__ = 'Попов Анатолий Викторович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

num = str(input('Please, enter a number: '))
max = 0
for i in num:
    if int(i) > max:
        max = int(i)
print(max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

num1 = int(input('Please, enter num1: '))
num2 = int(input('Please, enter num2: '))

num1, num2 = num2, num1

print ('num1: ', num1)
print ('num2: ', num2)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

from math import sqrt
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = b**2-4*a*c
if d < 0:
    print ('Nope')
elif d==0:
    x = -b/(2*a)
    print ('x = ', x)
elif d>0:
    x1 = (-b-sqrt(d))/(2*a)
    x2 = (-b+sqrt(d))/(2*a)
    print ('x1=', x1)
    print ('x2=', x2)


