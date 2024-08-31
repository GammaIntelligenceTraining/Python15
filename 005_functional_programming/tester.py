# def say_hello(name, surname):
# #     return f'Hello {name} {surname}!'
# #
# #
# # # print(say_hello('Roman', 'Kutselepa'))
# # x = say_hello('Roman', 'Kutselepa')
# # print(x)
#
# def short_or_long(string):
#     if len(string) > 5:
#         return 'long'
#     else:
#         return 'short'
#
# print(short_or_long('Interstellar'))
#
# words = ['Sun', 'Earth', 'Millenium', 'People', 'World']
# for word in words:
#     print(short_or_long(word))

# def fizz_buzz(start, end):
#     for num in range(start, end + 1):
#         if num % 3 == 0 and num % 5 == 0:
#             print(num, 'FIZZBUZZ')
#         elif num % 3 == 0:
#             print(num, 'FIZZ')
#         elif num % 5 == 0:
#             print(num, 'BUZZ')
#
#
# fizz_buzz(-100, 200)

# a = 1
# b = 2
# c = 3
#
# def sample():
#     a = 1000
#     print(a, b, c)
#
# sample()
# print(a, b, c)

# a = 100
#
#
# def sample(num):
#     print(a ** num)
#
#
# sample(2)

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area


def print_result():
    print(f'The area of triangle is {triangle_area(3, 4, 5)} cm2')


print_result()