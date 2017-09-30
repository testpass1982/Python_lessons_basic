# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
from fractions import Fraction

def fract_ops(fract):
    fract = fract.split(' ')
    fract1 = []
    fract2 = []
    for i in fract:
        if i=='+' or i=='-':
            fract1=fract[:fract.index(i)]
            fract2=fract[fract.index(i)+1:]
            operation = i
    result = operation, fract1, fract2
    return result

def return_fraction(arr):
    if len(arr)>1:
        if '-' not in arr[0]:
            result = Fraction(arr[0])+Fraction(arr[1])
        if '-' in arr[0]:
            result = Fraction(arr[0])+Fraction('-'+(arr[1]))
    else:
        return Fraction(arr[0])
    return result

def fract_calc(fract):
    fract = fract_ops(fract)
    if fract[0] == '+':
        result = return_fraction(fract[1])+return_fraction(fract[2])
    if fract[0] == '-':
        result = return_fraction(fract[1])-return_fraction(fract[2])
    str_result = str(result.numerator//result.denominator) + ' ' + str(result.numerator%result.denominator)+'/'+str(result.denominator)
    return str_result

print(fract_calc('5/6 + 4/7'))
print(fract_calc('-2/3 - -2'))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
