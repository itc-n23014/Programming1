A = {x for x in range(21) if x % 2 != 0}
print(A)

# 2つの集合を用いた例
A = {x for x in range(21)}  # 21までの整数が要素の集合
B = {y for y in range(21) if y % 2 == 0}  # 偶数が要素の集合
print(A - B)  # 集合A,Bの差を出力
