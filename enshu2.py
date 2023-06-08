# 演習問題2
# 組み込みinput()を使って、「2023」と入力してエンターを押すと、
# 「今は2023年です。来年は2024年です」と表示されるプログラムを作りましょう。

# ヒント
# 次のコードはエラー、文字列と数値は足し算できない (str関数が必要)
#print('今は' + 2023 + '年です')

# 次のコードもエラー、inputは、必ず文字列で受け取る
#year = input()
#print(year + 1)
# → # '2023' + 1 のような処理になり、エラー。
# 組み込み関数 int()が必要

nengo = input()
rainen = int(nengo) + 1
print('今は'+str(nengo)+'年です。来年は'+str(rainen)+'年です')

#これでも行ける
#print(f'今は{str(nengo)}年です。来年は{str(rainen)}年です')