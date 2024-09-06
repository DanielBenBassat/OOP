from shape import Shape
from square import Square


class Rectangle(Shape):
    """
    A class to represent a rectangle, inheriting from the Shape class.
    """
    def __init__(self, color, length, width):
        """
        Initialize a new Rectangle instance with a specific color, length, and width.

        :param color: The color of the rectangle.
        :param length: The length of the rectangle.
        :param width: The width of the rectangle.
        """
        super().__init__(color)
        self.length = length
        self.width = width

    def get_area(self):
        """
        Calculate the area of the rectangle.
        :return: the area of the rectangle
        """
        return self.length * self.width

    def get_perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        :return: The perimeter of the rectangle
        """
        return 2 * (self.length + self.width)

    def connect_rectangles(self, other):
        """
        Connect the current rectangle with another rectangle to create a new rectangle.
        :param other: another rectangle to connect with
        :return:  A new rectangle instance or none if other is not a rectangle
        """
        if isinstance(other, Rectangle):
            new_length = self.length + other.length
            new_width = self.width + other.width
            return Rectangle(self.color, new_length, new_width)

    def connect_rectangle_with_square(self, other):
        """
        Connect the current rectangle with square to create a new rectangle.
        :param other: square to connect with
        :return:  A new rectangle instance or none if other is not a square
        """
        if isinstance(other, Square):
            new_length = self.length + other.side
            new_width = self.width + other.side
            return Rectangle(self.color, new_length, new_width)