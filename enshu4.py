user_file_text = """
hoge
fuga
taro
ziro
saburo
"""
# この複数行のテキストを、splitメソッドでリストに分割し、アルファベット順に並び替えます。
# その後、joinメソッドを使い、print関数で
# fuga hoge saburo taro ziro
# と表示するプログラムを作成してください。


user_name_list = user_file_text.split()
user_name_list.sort()
print(user_name_list)
user_name_string = ' '.join(user_name_list)
#user_name_string = '\n'.join(user_name_list)
print(user_name_string)
