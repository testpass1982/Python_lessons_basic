# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
from ctypes.wintypes import HTASK

class Triangle():
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
    
    def sq(self):
        return abs(((self.x1-self.x3)*(self.y2-self.y3)-
                (self.x2-self.x3)*(self.y1-self.y3))/2)
        
    def ht(self, point):
        x = self.sq()
        if point == 1:
            ht = (2*x)/math.sqrt((self.x3-self.x2)**2 + (self.y3-self.y2)**2)
        if point == 2:
            ht = (2*x)/math.sqrt((self.x3-self.x1)**2 + (self.y3-self.y1)**2)
        if point == 3:
            ht = (2*x)/math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
        return ht
        
    def per(self):
        a = math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
        b = math.sqrt((self.x3-self.x2)**2 + (self.y3-self.y2)**2)
        c = math.sqrt((self.x3-self.x1)**2 + (self.y3-self.y1)**2)
        return a+b+c

tr = Triangle(2, 7, 3, 2, 6, 6)

print('Triangle square:' ,tr.sq())
print('Triangle ht: ', tr.ht(2))
print('Triangle perimeter', tr.per())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


A1 = (1, 1)
A2 = (2, 4)
A3 = (4, 4)
A4 = (5, 1)

def len_of(x1, y1, x2, y2):
    return abs(math.sqrt((x2-x1)**2 + (y2-y1)**2))


class Trapeze:
    def __init__(self, p1, p2, p3, p4):
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]
        self.x3 = p3[0]
        self.y3 = p3[1]
        self.x4 = p4[0]
        self.y4 = p4[1]

    def lengths(self):
        a = len_of(self.x3, self.y3, self.x2, self.y2)
        b = len_of(self.x4, self.y4, self.x1, self.y1)
        c = len_of(self.x2, self.y2, self.x1, self.y1)
        return a, b, c

    def check_is_trapezoid(self):
        if len_of(self.x1, self.y1, self.x3, self.y3) \
                == len_of(self.x2, self.y2, self.x4, self.y4) \
                and len_of(self.x2, self.y2, self.x4, self.y4) == \
                        len_of(self.x3, self.y3, self.x1, self.y1):
            return True
        else:
            print('it is not trapezoid')
            return False

    def per(self):
        if self.check_is_trapezoid():
            a = len_of(self.x3, self.y3, self.x2, self.y2)
            b = len_of(self.x4, self.y4, self.x1, self.y1)
            c = len_of(self.x2, self.y2, self.x1, self.y1)
            return a+b+2*c
        else:
            print ('it is not trapezoid')

    def sq(self):
        if self.check_is_trapezoid():
            a = len_of(self.x3, self.y3, self.x2, self.y2)
            b = len_of(self.x4, self.y4, self.x1, self.y1)
            c = len_of(self.x2, self.y2, self.x1, self.y1)
            return ((a+b)/4)*math.sqrt(4*c**2-(a-b)**2)
        else:
            print('it is not trapezoid')

trp = Trapeze(A1, A2, A3, A4)
print('We check if figure is trapezoid: ', trp.check_is_trapezoid())
print('Lengths of sides: a = {}, b = {}, c = {}'.format(trp.lengths()[0], trp.lengths()[1], trp.lengths()[2]))
print('Perimeter of trapezoid is: ', trp.per())
print('Square of trapezoid is: ', trp.sq())