from shape import Shape
from square import Square


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def connect_rectangles(self, other):
        if isinstance(other, Rectangle):
            new_length = self.length + other.length
            new_width = self.width + other.width
            return Rectangle(self.color, new_length, new_width)

    def connect_rectangle_with_square(self, other):
        if isinstance(other, Square):
            new_length = self.length + other.side
            new_width = self.width + other.side
            return Rectangle(self.color, new_length, new_width)