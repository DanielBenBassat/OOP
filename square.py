from shape import Shape


class Square(Shape):
    """
    A class to represent a square, inheriting from the Shape class.
    """
    def __init__(self, color, side):
        """
        Initialize a new Square instance with a specific color and side length.
        :param color: The color of the square.
        :param side:  The length of one side of the square.
        """
        super().__init__(color)
        self.side = side

    def get_area(self):
        """
        Calculate and return the area of the square.
        :return: the area of the square
        """
        return self.side * self.side

    def get_perimeter(self):
        """
        Calculate and return the perimeter of the square.
        :return: the perimeter of the square.
        """
        return 4 * self.side

    def connect_squares(self, other):
        """
        Connect the current square with another square to create a new square.
        :param other: another square to connect with
        :return: A new square instance with the combined side length or none if ather is not a square
        """
        if isinstance(other, Square):
            new_side = self.side + other.side
            return Square(self.color, new_side)