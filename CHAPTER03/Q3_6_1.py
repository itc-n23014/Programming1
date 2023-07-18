from random import sample

str4 = "".join(sample([str(i) for i in range(10)], k=4))
while str4 != (val := input()):
    print(val, ": NG", sep="")
print("OK")
