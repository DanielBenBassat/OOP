from shape import Shape


class Circle(Shape):
    """
    A class to represent a circle, inheriting from the Shape class.
    """
    def __init__(self, color, radius):
        """
        Initialize a new Circle instance with a specific color and radius.
        :param color:  The color of the circle
        :param radius: The radius of the circle.
        """
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        """
        Calculate and return the area of the circle.
        """
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        """
        Calculate and return the perimeter of the circle.
        """
        return 2 * 3.14 * self.radius