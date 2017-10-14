# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
from ctypes.wintypes import HTASK

class Triangle(object):
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

print(tr.sq())
print(tr.ht(3))
print(tr.per())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze(Object):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        
    def check_if_trapeze(self):
        pass
        
    