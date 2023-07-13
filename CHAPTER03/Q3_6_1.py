from random import sample

str4 = "".join(sample([str(i) for i in range(10)], k=4))
a = 0
while a == 0:
    num4 = input()
    a = 1 if num4 == str4 else 0
    print("OK") if a == 1 else print(f"{num4}:  NG")
