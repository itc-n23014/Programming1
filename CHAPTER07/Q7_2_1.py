def f(list_, index):
    try:
        del list_[index]
    except IndexError:
        print("Index Not Found")
    except:
        print("Unexpected Error")
    else:  # tryが正常に終了
        print("Successfully")


my_list = "a,b,c,d".split(",")
f(my_list, "5")
f(my_list, 5)
f(my_list, 0)
print(my_list)
