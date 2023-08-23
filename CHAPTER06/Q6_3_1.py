class Nigiri:
    category = "にぎり"
    top = "ネタ"
    base = "しゃり"

    def show_attributes(self):
        print(f"top: {self.top}, base: {self.base}, category: {self.category}")


class Katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とネギ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print(f"price: {self.price}\ntopping: {self.topping}")


k1 = Katsuo()
k1.show_attributes()
