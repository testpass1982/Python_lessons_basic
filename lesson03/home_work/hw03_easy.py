# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    rounded_arr = str(number)
    rounded_arr = rounded_arr.split('.')
    res = rounded_arr[1]
    for i in res:
        if res.index(i) < ndigits and int(res[res.index(i)+1]) >= 5:
            result = int(res[:ndigits])+1
        elif res.index(i) < ndigits and int(res[res.index(i)+1]) < 5:
            result = int(res[:ndigits])
        elif ndigits == 0:
            result = 0
    rounded_arr[1] = str(result)
    if result%10**ndigits==0 and ndigits!=0:
        rounded_arr[0]=int(rounded_arr[0])+1
        rounded_arr[0] = str(rounded_arr[0])
        rounded_arr.pop(1)
    rounded_arr = ".".join(rounded_arr)
    return float(rounded_arr)
print('my_round:')
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
#для сравнения:
print('round:')
print(round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
def lucky_ticket(ticket_number):
    ticket_number=str(ticket_number)
    arr1=[]
    arr2=[]
    if len(ticket_number)==6:
        for i in range(0, int(len(ticket_number)/2)):
            if str.isdigit(str(i)):
                arr1.append(int(ticket_number[i]))
            else:
                result = False
        for i in range(int(len(ticket_number)/2), int(len(ticket_number))):
            if str.isdigit(str(i)):
                arr2.append(int(ticket_number[i]))
            else:
                result = False
        if sum(arr1) == sum(arr2):
            result = True
        else:
            result = False
    if len(ticket_number)!=6:
        result = False
    return result
    
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
