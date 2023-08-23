class Rectangle:
    angle = 90

    def __init__(self, width, height):
        self.name = "rectangle"
        self.width = width
        self.height = height
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        w = self.width
        h = self.height
        return (w + h) * 2

    def calc_area(self):
        w = self.width
        h = self.height
        return w * h

    def show_attributes(self):
        ang = self.angle
        n = self.name
        w = self.width
        h = self.height
        p = self.perimeter
        a = self.area
        print(f"name: {n}, width: {w}, height: {h}, angle: {ang}")
        print(f"perimeter: {p}, area: {a}")


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)
        self.name = "square"


s1 = Square(4)
s1.show_attributes()
