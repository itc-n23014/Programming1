A = {x for x in "abcabcabc" if x not in "ab"}  # 'c'の集合
B = {y for y in "abcabcabc" if y not in "bc"}  # 'a' の集合
print(A | B)  # A,Bの和集合なので、{'a','c'} となる

# intersectionメソッドを用いた例
print(A.union(B))
