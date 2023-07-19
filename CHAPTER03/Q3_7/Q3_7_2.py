with open("number.txt", "r") as f:
    sum = 0
    for data in f:
        num = int(data)
        sum += num
    print(sum)  # 指定ファイルに記述された数字の和「55」が出力される
