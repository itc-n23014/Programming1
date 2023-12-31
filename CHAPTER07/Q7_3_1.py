refference = {1: "red", 2: "blue", 3: "yellow", 4: "green", 5: "purple"}


class MyDictkeyError(Exception):
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return f"辞書にkeyが登録されていません {self.key}"


def get_dict_value(dict_tbl, key):
    if key not in dict_tbl:
        raise MyDictkeyError(key)
    else:
        return dict_tbl[key]


my_dict = {1: "red", 2: "blue", 3: "yellow"}

try:
    my_col = get_dict_value(my_dict, 5)
except MyDictkeyError as err:
    print(err)
    key = err.args[0]
    my_dict[key] = refference[key]
    print(key, refference[key], "をmy_dictに追加")
    my_col = key, refference[key]

my_col
