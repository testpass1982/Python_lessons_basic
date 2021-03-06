# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

def sq_gen(lst):
    result = [x**2 for x in lst]
    return result

print(sq_gen([1, 2, 4, 0]))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

def tut_fruit(lst1, lst2):
    result = [x for x in lst1 if x in lst2]
    return result

fruits1 = ['apple', 'orange', 'pineapple', 'banana', 'cherry']
fruits2 = ['orange', 'banana', 'melon', 'cherry']

print(tut_fruit(fruits1, fruits2))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

def my_filter(x):
    if x%3==0 and x>=0 and x%4!=0:
        return True

lst = [1, 4, 3, 15, 28, -30, -27, 12, 24, 48, 33]
lst1 = [x for x in lst if my_filter(x)]

print('lst: ', lst)
print('lst1: ', lst1)