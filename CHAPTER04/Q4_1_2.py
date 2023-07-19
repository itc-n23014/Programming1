def f(n):
    r = [0, 1]
    while (a := r[-2] + r[-1]) < n:
        r.append(a)
    return r


print(f(1000))
