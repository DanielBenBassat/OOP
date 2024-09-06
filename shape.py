class Shape:
    """
    the class represent a geometric shape with a color attribute.
    """
    def __init__(self, color):
        """
        Initialize a new Shape instance with a specific color.
        :param color: the color of the shape
        """
        self.color = color

    def set_color(self, color):
        """
        Set a new color for the shape.

        :param color: the new color of the shape
        :return: none
        """
        self.color = color

    def get_color(self):
        """
        Get the current color of the shape.

        :return: str of the current color of the shape.
        """
        return self.color



