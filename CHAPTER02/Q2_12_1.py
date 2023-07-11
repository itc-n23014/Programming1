import math

# モジュールのpow関数は,引数をfloat型にして実行するため,「8.0」が出力される
print(math.pow(2, 3))

# 組み込み演算子を使った場合,通常のint型で,「8」が出力
print(2**3)
