# name = input('Enter name: ')
# surname = input('Enter surname: ')
# age = input('Enter age: ')

# name, surname, age = input('Enter name, surname, age (use coma as separator): ').split(', ')
#
# print(f'Hello, {surname} {name}. Your age is: {age}')
# print('Hello, ' + surname + ' ' + name + '. Your age is: ' + age)
#

# import math
#
# side_a = float(input('Enter side A: '))
# side_b = float(input('Enter side B: '))
#
# # c = (side_a ** 2 + side_b ** 2) ** 0.5
# c = math.sqrt(side_a ** 2 + side_b ** 2)
#
# print(c)
#
# x = 90
# x = math.radians(x)
# print(math.sin(x))
# x = math.degrees(x)

# side_a = float(input('Enter side A: '))
# side_b = float(input('Enter side B: '))
# side_c = float(input('Enter side C: '))
#
# if side_c ** 2 == side_a ** 2 + side_b ** 2:
#     print('It is a Right triangle')
# else:
#     print('It is not a Right triangle')

# user_lst = input('Enter some values, use coma as separator: ').split(', ')
# for item in user_lst[::-1]:
#     print(item)

# tup_a = (1, 2, 3, 5, 8)
# tup_b = (8, 2, 5)

# tup_a = tup_a[:2] + tup_b + tup_a[2:]
# print(tup_a)

# tup_a = list(tup_a)
# for x in tup_b[::-1]:
#     tup_a.insert(2, x)
#
# tup_a = tuple(tup_a)
# print(tup_a)

# test_lst = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6]
# result = {}
#
# for number in test_lst:
#     result[number] = test_lst.count(number)
#
# res = []
# for key in result.keys():
#     if result[key] == max(result.values()):
#         res.append(key)
#
# print(res)
# print(result.values())

# max_count = 0
# result = []
#
# for number in test_lst:
#     if test_lst.count(number) > max_count:
#         max_count = test_lst.count(number)
#
# for number in test_lst:
#     if test_lst.count(number) == max_count:
#         if number not in result:
#             result.append(number)
#
# print(result)

seconds = 123123


def format_time():
    global seconds
    days = seconds // (24 * 60 * 60)
    seconds %= (24 * 60 * 60)
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60

    print(f'{days}:{hours}:{minutes}:{seconds}')


format_time()
