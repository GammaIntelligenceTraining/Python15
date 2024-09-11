import itertools

# counter = itertools.count(100, -50)
# counter = itertools.cycle(['On', 'Off'])
# counter = itertools.repeat(0)
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# #
# x = [1, 2, 3]
# y = [4, 5, 6, 7]
# res = zip(x, y, counter)
# print(list(res))
# # print(list(itertools.zip_longest(x, y)))

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]

# # NO ORDER, NO DUPLICATES
# result = itertools.combinations(letters, 2)
# for comb in result:
#     print(comb)

# # ORDER, NO DUPLICATES
# result = itertools.permutations(letters, 2)
# for comb in result:
#     print(comb)

# # ORDER, DUPLICATES
# result = itertools.product(letters, repeat=2)
# for comb in result:
#     print(comb)

# # NO ORDER, DUPLICATE
# result = itertools.combinations_with_replacement(letters, 2)
# for comb in result:
#     print(comb)

# numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
# selectors = [True, False, False, True]

# result = itertools.compress(letters, selectors)
# for item in result:
#     print(item)

# result = itertools.filterfalse(lambda x: x > 2, numbers2)
# for item in result:
#     print(item)

# result = itertools.dropwhile(lambda x: x > 2, numbers2)
# result = itertools.takewhile(lambda x: x > 2, numbers2)
# for item in result:
#     print(item)


# numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
# result = map(lambda x: x ** 2, numbers2)
# for res in result:
#     print(res)

people = [
    {
        'name': 'Jack',
    },
    {
        'name': 'Sarah',
    },
    {
        'name': 'Bob',
    },
]


def add_len(obj):
    return {
        'name': obj['name'],
        'name_length': len(obj['name'])
    }


result = map(add_len, people)
print(list(result))