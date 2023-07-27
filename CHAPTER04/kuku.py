n = int(input("どの段までの表を出しますか: "))
m = len(str(n * 9))
f = [" ".join([f"{i*j:{m}d}" for j in range(1, n + 1)]) for i in range(1, 10)]

print("\n".join(f))
