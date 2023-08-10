A = {x for x in range(21)}
B = {y for y in range(21) if y % 2 == 0}
C = A - (A & B)  # 21まで整数集合からA,Bの部分集合を引く
print(C)  # 奇数で構成された集合ができる

# differenceメソッドを用いた例
C = A.difference(B)
print(C)
