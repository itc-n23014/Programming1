def f(*nums):
    return [i**2 for i in nums]


print(f(*[1, 2, 3, 4]))
print(f(*list(range(100))))
