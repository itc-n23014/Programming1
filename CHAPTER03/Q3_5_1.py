a = 1
while a < 10:
    if a % 2 == 0:
        print(a)
    a += 1

# 内包表記を用いた例
print(*[i for i in range(2, 10)][::2], sep="\n")
