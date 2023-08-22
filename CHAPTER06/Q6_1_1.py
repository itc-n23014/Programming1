class Cat:
    animal = "Cat"
    cry = "Meow"
    legs = 4
    is_animal = True


tama = Cat()
print(
    """動物: {}
鳴き声: {}
足の数: {}
動物: {}""".format(
        tama.animal, tama.cry, tama.legs, tama.is_animal
    )
)
