def f(n=100):
    list = [3, 0, 2]
    a, b, c = 3, 0, 2
    while a < n:
        list.append(a)
        a, b, c = b, c, a + b
    return list


print(f())
