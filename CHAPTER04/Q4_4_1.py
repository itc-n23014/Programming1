# グローバル関数を使った例
n = 0


def vote():
    print("投票します")
    global n
    n += 1


def reset():
    global n
    print("箱を空にします")
    n = 0


def check():
    global n
    print("票の数は{}です".format(n))


while True:
    a = input("vote or reset or check: ")
    if a == "vote":
        vote()
    elif a == "reset":
        reset()
    else:
        check()
