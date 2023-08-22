class Person:
    def __init__(self, name="", nationality="", birth="", address=""):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("NAME:", self.name)
        print("NATIONALITY:", self.nationality)
        print("BIRTH:", self.birth)
        print("ADDRESS:", self.address)


heroine = Person("かぐや姫", "日本", "685", "静岡県富士市")
heroine.show_attributes()

me = Person("光彦", "日本", "2001", "沖縄県那覇市")
me.show_attributes()
