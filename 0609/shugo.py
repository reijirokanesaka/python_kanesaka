# リストの重複した値を消すのに、集合はよく使います。
number_list = [1, 1, 2, 3, 2, 5, 5, 6, 7, 7]

# 組み込み関数setを使うと、リスト等を集合に変換できる
# 集合は重複を許さないので、重複した値が消える
number_set = set(number_list)
print(number_set)