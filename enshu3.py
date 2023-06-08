# 演習問題1.
# data_list = [1, 2, [3, 4, 5], [6, 7], 8, 9, [10, 11]]
# 上のリストから、「7」をprint関数で取り出してください。

data_list = [1, 2, [3, 4, 5], [6, 7], 8, 9, [10, 11]]
print(data_list[3][1])

# 演習問題2.
# 空のリストを定義し、組み込み関数input()を3回呼び出して数値を入力し、空のリストに数値を追加してください。
# そのリストをprint()関数で表示しますが、その際に sortメソッドを使ってソートされて表示するようにしてください。（昇順、小さい数値が先に表示される）

user_list = []
user_input_number = input()
user_list.append(int(user_input_number))
user_input_number = input()
user_list.append(int(user_input_number))
user_input_number = input()
user_list.append(int(user_input_number))
# user_list.sort()
# print(user_list)
print(user_list.sort())

# 演習問題3.
# 空のリストを定義し、組み込み関数input()を3回呼び出して数値を入力し、空のリストに数値を追加してください。その際appendメソっドではなくinsertメソッドを使ってください。
# そのリストをprint()関数で表示しますが、その際に組み込み関数sortedを使ってソートされて表示するようにしてください。（降順、大きい数値が先に表示される）

user_list = []
user_input_number = input()
user_list.insert(0, int(user_input_number))
user_input_number = input()
user_list.insert(1, int(user_input_number))
user_input_number = input()
user_list.insert(2, int(user_input_number))
user_list.sort(reverse=True)
print(user_list)