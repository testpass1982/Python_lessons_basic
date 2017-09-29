# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_arr = [1, 1]
    fib1 = 1
    fib2 = 1
    i = 2
    while i < m:
        fib_sum = fib2+fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        fib_arr.append(fib_sum)
    return fib_arr[n:]

print(fibonacci(5, 15))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for blob in range (len(origin_list)-1, 0, -1):
        for i in range (blob):
            if origin_list[i]>origin_list[i+1]:
                temp = origin_list[i]
                origin_list[i] = origin_list[i+1]
                origin_list[i+1]=temp
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(f, iterable):
    if f != None:
        result = [item for item in iterable if f(item)]
    else:
        result = [item for item in iterable if item]
    return result

def f(x):
    return x%2!=0

def f1(x):
    return x<0

def f2(x):
    return str.isdigit(str(x))==False

print(my_filter(f, [14, 15, 16, 18, 19, 21]))
print(my_filter(f1, [-14, 15, -16, 18, 19, 21]))
print(my_filter(f2, [14, 19, 'test', 21, 'woop']))
print(my_filter(None, [-14, 19, 21, 'test', 'woop']))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

A1=(1, 1)
A2=(2, 4)
A3=(7, 4)
A4=(6, 1)

def is_par(bl, tl, tr, br):
    if br[0]-bl[0] == tr[0]-tl[0] and tl[1]-bl[1] == tr[1]-br[1]:
        return True
    else:
        return False
print(is_par(A1, A2, A3, A4))