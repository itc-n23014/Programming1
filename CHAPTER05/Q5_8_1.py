country_code = {
    "Iceland": {"code": "354", "capital": "Reykjavik"},
    "Ireland": {"code": "353", "capital": "Dublin"},
    "Azerbaijan": {"code": "994", "capital": "Baku"},
}


def getstr_keyval(x):
    if isinstance(x, dict):
        return " ".join([str(key) + " " + getstr_keyval(val) for key, val in x.items()])
    return x


for key, val in country_code.items():
    # 辞書変数内の順序はキーのハッシュ値で、順・行不同となる
    print(key, getstr_keyval(val))
