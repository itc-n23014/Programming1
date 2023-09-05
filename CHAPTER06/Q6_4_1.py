import random
from itertools import islice

random.seed(1)
msgs = "Hi,Hello,Good morning,See you later,How are you,Have a good day".split(",")
with open("some.txt", "w") as f:
    f.writelines("{}, {}\n".format(i, random.choice(msgs)) for i in range(1000000))

with open("some.txt") as f:
    for line in islice(f, 3):
        print(line, end="")
