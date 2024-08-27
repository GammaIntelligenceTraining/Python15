# empty = []
# empty = list()
# print(type(empty))  # list()
# print(bool(empty))  # empty list give false value

# x = 10
#
# filled = [123, 0.123, 'hello', x, [1, 2, [3, 4, 5], 6], True, True, True]
# print(len(filled))
# # print(filled[4][2][1])
#
# print(len(filled[4]))

courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'english', '123124']

# [START:END:STEP]
# print(courses[1:4])
# print(courses[::-3])
# print(courses[-1])

# courses[0] = 'Art'
# print(courses[0])
# courses[0] = 'English'
# print(courses[0])

# courses.append([1, 2, 3, 4])
# print(courses)
# courses.insert(0, 'English')
# print(courses)
# courses.extend(['Art', 'Economics'])
# print(courses)

# courses.remove('Math')
# print(courses)
# courses.pop()
# print(courses)
# print(courses.reverse())
# print(courses)

# courses.sort()
# print(courses)
#
# numbers = [45, 23, 12.32, 9.043, 24]
# numbers.sort(reverse=True)
# print(numbers)

# print(min(courses))
# print(max(courses))
# print(min('Hello world!'))
# print(max('Hello world!'))
# print(sum([123, 123, 543, 23, 231]))

# print('Math' in courses)
# print('world' in 'Hello world!')
#
# print('hello people, of planet, earth!'.split(', '))
#
# user_input = input('Enter something: ')  # always returns a string
# print(user_input.split(', '))
# sep = 123
# print(str(sep).join(courses))

# a = 'one'
# b = a
# a += 'two'
# print(a, b)

# a = [1, 2, 3, 4, 5]
# print(id(a))
# b = a.copy()
# print(id(b))
# a.append(555)
# b.append(777)
# print(a)
# print(b)

# empty = ()
# empty = tuple()
# print(type(empty))  # tuple()
#
# x = (1, )
# print(type(x))

# courses = ('History', 'Math', 'Literature', 'Physics', 'Programming', 'english', '123124')
# print(courses[0])
# # courses[0] = 'Art'
# print(courses.count('Math'))
# print(courses.index('Math'))
# courses = list(courses)
# courses.append('Art')
# courses = tuple(courses)
# print(courses)

# print([1, 2, 3] + [3, 2, 1])
# print((1, 2, 3) + (3, 2, 1))

x = set()  # set()
print(type(x))

courses = {'History', 'Math', 'Math', 'Math', 'Math', 'Literature', 'Physics', 'Programming', 'english', '123124'}
courses2 = {'Math', 'Economics', 'History', 'Spanish'}
print(courses.difference(courses2))
print(courses2.difference(courses))

print(courses.intersection(courses2))

