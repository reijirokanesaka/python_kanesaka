#FizzBazz

# def FizzBazz (a = None, b = None):
#     if a is not None and b is not None:
#         for i in range(a, b + 1):
#             if i % 15 == 0:
#                 print('FizzBazz')
#             elif i % 3 == 0:
#                 print('Fizz')
#             elif i % 5 == 0:
#                 print('Bazz')
#             else:
#                 print(i)
#     else:
#         for i in range(1, 101):
#             if i%15 == 0:
#                 print('FizzBazz')
#             elif i%3 == 0:
#                 print('Fizz')
#             elif i%5 == 0:
#                 print('Bazz')
#             else:
#                 print(i)

def FizzBazz (a = 1, b = 100):
    for i in range(a, b + 1):
        if i % 15 == 0:
            print('FizzBazz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Bazz')
        else:
            print(i)


FizzBazz(1, 50)
print('---------------------------------')
FizzBazz()