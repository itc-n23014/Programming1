my_list = [i + 1 for i in range(10)]
reverse_even = [i for i in my_list[::-1] if i % 2 == 0]
print(reverse_even)
