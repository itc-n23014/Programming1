class Cylinder:
    pi = 3.14

    def __init__(self, radius=1, height=1):
        self.radius = float(radius)
        self.height = float(height)

    def base(self):
        return (self.radius**2) * Cylinder.pi

    def area(self):
        surface = self.height * (self.radius * 2 * Cylinder.pi)
        return surface + 2 * self.base()

    def volume(self):
        return self.base() * self.height

    def result(self):
        print(f"半径: {a}\n高さ: {b}\n表面積: {self.area()}\n体積: {self.volume()}")


a = float(input("半径を入力してください: "))
b = float(input("高さを入力してください: "))
c1 = Cylinder(a, b)
c1.result()
