a = int(input())  # aの値を入力
a = a * 2 if a >= 100 else (a / 2 if a >= 50 else a + 2)
print(a)
