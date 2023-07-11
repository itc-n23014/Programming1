# モジュールをimportしていないのでエラーが起きる
print(random.randint(0, 10))

# 正しいモジュールの使い方
import random 
print(random.randint(0, 10))
