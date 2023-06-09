# FizzBazz
# for i in range(1, 101):
#     if i%15 == 0:
#         print('FizzBazz')
#     elif i%3 == 0:
#         print('Fizz')
#     elif i%5 == 0:
#         print('Bazz')
#     else:
#         print(i)

# 素数の判定
# 1から100まで繰り返し、素数の数値を表示するプログラムを作成しましょう。

for i in range(1, 101):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i)

# for i in range(2, 101):
#     is_prime = True  # 素数かどうかのフラグ
#     # i = 10
#     # 2~9までで、割ってみて
#     # 割れきれたら素数じゃない
#     # print(f'i={i}')
#     for j in range(2, i):
#         # print(f'  j={j}')
#         if i % j == 0:
#             is_prime = False
#
#     if is_prime:
#         print(i)
