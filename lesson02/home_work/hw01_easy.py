
__author__ = 'Попов Анатолий Викторович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

# Неправильно понял задачу
# num = int(input('Enter your number: '))
# i = 0
# while i <= num:
#     print (i)
#     i+=1
#
# num1 = int(input('Enter your next number: '))
# for i in range(0, num1+1):
#     print(i)

#вот правильное решение:
num = str(input('Enter your number: '))
for i in range(0, len(num)):
    print(num[i])

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = a
a = b
b = c
print ('Now we switch them!')
print ('First number is ', a)
print ('Second number is ', b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Enter your age to login: '))
if age < 18:
    print ('Sorry, only adults allowed...')
else:
    print('Access granted!')
