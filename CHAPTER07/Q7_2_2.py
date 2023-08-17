def square(x):
    if isinstance(x, str) and x.isdigit():
        x = int(x)
    elif not isinstance(x, (int, float)):
        raise ValueError("square", x)
    return x**x


x = input("二乗する値を入力してください: ")
print(square(x))
