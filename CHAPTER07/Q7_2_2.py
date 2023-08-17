def square(x):
    try:
        x = float(x)
        return x * x
    except:
        return "TypeError"


x = input("二乗する値を入力してください: ")
print(square(x))
