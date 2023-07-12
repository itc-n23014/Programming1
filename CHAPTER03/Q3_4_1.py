for i in range(10):
    if i % 2 == 0:
        continue  # 偶数の場合、処理をスキップ
    print(i)  # 奇数だけが出力される


for i in range(10):
    if i % 2 == 0:
        break  # 偶数の場合、ループ停止
    print(i)  # 最初の0でbreakとなり、何も出力されない


# 内包表記を用いた例
print("\n".join([str(i) for i in range(10) if i % 2 != 0]))
