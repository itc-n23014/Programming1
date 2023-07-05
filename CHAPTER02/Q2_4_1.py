b = []
a = 23
while a != 0:
    b.append(a % 2)
    a //= 2
print(*b[::-1])
