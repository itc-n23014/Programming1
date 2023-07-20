from random import sample

num = sample([str(i) for i in range(10)], k=4)
val = 0
while (val := val) != num:
    val = [i for i in input("input 4 numbers: ")]
    list = [val[i] if val[i] == num[i] else "X" for i in range(4)]
    print("-> " + "".join(list))
