def f(x):
    try:
        return sum(x) / len(x)
    except:
        return "リストに要素が入っていません"


x = input("数値を入力してください(カンマ区切り): ")
x = list(map(float, x.split(","))) if x else []
print(f(x))
