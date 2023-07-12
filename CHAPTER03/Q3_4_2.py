numbers = [1, 1, 2, 3, 5, 8, 13, 21]
x = []
for n in numbers:
    if n > 10:
        break
    x.append(n)
# リストの8までの合計値なので、「20」が出力される
print(sum(x))
