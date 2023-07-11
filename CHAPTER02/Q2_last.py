from random import randint

alpha = [chr(i).upper() for i in range(97, 97 + 26)]

# イニシャル"K"に一致した時、終了
while True:
    a = alpha[randint(0, 25)]
    print(a)
    if a == "K":
        break

# イニシャル"M_K"に一致したとき終了
while True:
    a = alpha[randint(0, 25)]
    b = alpha[randint(0, 25)]
    print(f"{a}_{b}")
    if a == "M" and b == "K":
        break
