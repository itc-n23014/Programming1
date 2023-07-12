my_list = [1, 1, 2, 3, 5, 8, 13]
x = 0
x += sum(n for n in my_list if n % 2 != 0)  # 奇数の要素だけxに足していく
print(x)
