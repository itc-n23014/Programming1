b = []
a = 23
while True:
    b.append(a % 2)
    a //= 2
    if a == 0:
        break
print(*b[::-1])
