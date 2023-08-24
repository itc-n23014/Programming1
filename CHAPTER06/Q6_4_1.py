import random

%%time


random.seed(1)
msgs = 'a,b,c,d'.split(',')

with open('some.txt', 'w') as f:
    for i in range(10000):
        f.write("{},{}\n".format(i, random.choice(msgs)))

with open('some.txt', 'r') as f:
    for c, l in enumerate(f):
        print(l, end=" ")
        if c == 2:
            break
