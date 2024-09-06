import random
from square import Square
from rectangle import Rectangle
from circle import Circle

List_OF_COLOR = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]


class Container:
    def __init__(self):
        self.list_of_shapes = []

    def generate(self, num):
        for i in range(num):
            x = random.randint(1, 3)
            color = List_OF_COLOR[random.randint(0, len(List_OF_COLOR)-1)]
            if x == 1:
                new_shape = Square(color, random.randint(1, 10))
            elif x == 2:
                new_shape = Rectangle(color, random.randint(1, 10), random.randint(1, 10))
            else:
                new_shape = Circle(color, random.randint(1, 10))
            self.list_of_shapes.append(new_shape)

    def sum_areas(self):
        sum_of_areas = 0
        for shape in self.list_of_shapes:
            sum_of_areas += shape.get_area()
        return sum_of_areas

    def sum_perimeters(self):
        sum_of_perimeters = 0
        for shape in self.list_of_shapes:
            sum_of_perimeters += shape.get_perimeter()
        return sum_of_perimeters

    def count_colors(self):
        dict_of_colors = {}
        for color in List_OF_COLOR:
            dict_of_colors[color] = 0

        for shape in self.list_of_shapes:
            color = shape.get_color()
            dict_of_colors[color] += 1
        return dict_of_colors
