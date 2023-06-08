#inputの使い方

user_input_name = input()
result = f'こんにちは、{user_input_name}'
# result = 'こんにちは、' + user_input_name
print(result)

# もうちょい古い書き方。formatで、変数を埋め込める
# 'こんにちは{}'.format(user_input_name)