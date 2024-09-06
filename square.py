from shape import Shape


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side

    def connect_squares(self, other):
        if isinstance(other, Square):
            new_side = self.side + other.side
            return Square(self.color, new_side)