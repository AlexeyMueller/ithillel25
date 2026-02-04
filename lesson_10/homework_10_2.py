"""Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі
та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""

import math
from abc import ABC, abstractmethod
class Figure (ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Figure):
    def __init__(self, base, height, side_c):
        self.base = base
        self.height = height
        self.side_c = side_c


    def area(self):
        area_tri_base = 0.5 * self.base * self.height
        return area_tri_base

    def perimeter(self):
        p = self.base + self.height + self.side_c
        return p



class Square(Figure):
    def __init__(self, a):
        self.a = a

    def area(self):
        area_square = self.a * self.a
        return area_square

    def perimeter(self):
        p_square = 4 * self.a
        return p_square


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area_rectangle = self.length * self.width
        return area_rectangle

    def perimeter(self):
        p_rectangle = 2 * (self.length + self.width)
        return p_rectangle


all_figures = [Triangle(5, 7, 8.6), Square(5), Rectangle(4, 9)]
for i in all_figures:
    print(i.area())
    print(i.perimeter())


tri = Triangle(5, 7, 8.6)
sq = Square (5)
rec = Rectangle(4, 9)










