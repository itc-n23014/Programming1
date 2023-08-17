def f(table, key):
    try:
        return table[key]
    except:
        return "key is not found"


name_age = {"tanaka": 35, "satou": 25, "suzuki": 27}
n = input("名前を入力してください: ")
print(f(name_age, n))
