from select import select
from turtle import color
import math

class Figure:
    def __init__(self, color = [], sides = [], filled = False, sides_count = 0):
        if len(sides) != sides_count:
            sides = [1] * sides_count
        self.__color = color
        self.__sides = sides
        self.filled = filled
        self.sides_count = sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return r, g, b
        else:
            return self.__color


    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)
        self.__color = list(new_color)
        return self.__color

    def __is_valid_sides(self,sides):
        valid = True
        for side in sides:
            if side <= 0 and isinstance(side, int) != True:
                valid = False
        if len(sides) == self.sides_count and valid:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):  #площадь фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        i = len(self.__sides) - 1
        if self.__is_valid_sides(new_sides):
            for sid in new_sides:
                self.__sides[i] = sid
                i += 1

class Circle(Figure):
    def __init__(self, color = [], sides = [], filled = True, sides_count = 1):
        super().__init__(color, sides, filled, sides_count)
        self.radius = sides[0] / 2

    def get_square(self):
        return math.pi * math.pow(self.radius, 2)

class Triangle(Figure):
    def __init__(self, color = [], sides = [], filled = True, sides_count = 3):
        super().__init__(color, sides, filled, sides_count)

    def get_square(self):
        p = self.__len__() / 2
        return math.sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))

class Cube(Figure):
    def __init__(self, color = [], sides = [], filled = True,  sides_count = 12):
        cube_sides = sides * sides_count
        super().__init__(color, cube_sides, filled, sides_count)

    def get_volume(self):
        return math.pow(self._Figure__sides[0], 3)


circle1 = Circle([200, 200, 100], [10])
cube1 = Cube([222, 35, 130], [6])
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())