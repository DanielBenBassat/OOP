from square import Square
from rectangle import Rectangle
from circle import Circle
from container import Container


def main():
    my_container = Container()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':

    c = Circle("yellow", 2)
    assert c.get_perimeter() == 12.56
    assert c.get_area() == 12.56

    s1 = Square("blue", 4)
    s2 = Square("red", 3)
    s3 = s1.connect_squares(s2)
    assert s3.get_area() == 49
    assert s3.get_perimeter() == 28
    assert s3.get_color() == s1.get_color()

    r1 = Rectangle("blue", 4, 3)
    r2 = Rectangle("red", 3, 1)
    r3 = r1.connect_rectangles(r2)
    assert r3.get_area() == 28
    assert r3.get_perimeter() == 22
    assert r3.get_color() == r1.get_color()

    new_shape = r1.connect_rectangle_with_square(s1)
    assert new_shape.get_area() == 56
    assert new_shape.get_perimeter() == 30

    assert s1.connect_squares(r1) is None
    assert r1.connect_rectangles(s1) is None

    my_container1 = Container()
    my_container1.generate(100)
    counter = 0
    for color in my_container1.count_colors():
        counter += my_container1.count_colors()[color]
    assert counter == 100
    main()