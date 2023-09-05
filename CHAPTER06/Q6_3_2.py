class Rectangle:
    angle = 90

    def __init__(self, width, height):
        self.name = "rectangle"
        self.width = width
        self.height = height
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        return (self.width + self.height) * 2

    def calc_area(self):
        return self.width * self.height

    def show_attributes(self):
        print(
            f"name: {self.name}, width: {self.width}, height: {self.height}, angle: {self.angle}"
        )
        print(f"perimeter: {self.perimeter}, area: {self.area}")


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)
        self.name = "square"


s1 = Square(4)
s1.show_attributes()
