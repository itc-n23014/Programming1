f = [sum, min, max]
a = range(1, 11)
print(*[f"Func: {i.__name__}, result: {i(a)}" for i in f], sep="\n")
