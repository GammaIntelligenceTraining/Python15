test_lst = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10]

max_count = 0
new_lst = []

for num in test_lst:
    if test_lst.count(num) > max_count:
        max_count = test_lst.count(num)

for num in test_lst:
    if test_lst.count(num) == max_count and num not in new_lst:
        new_lst.append(num)
#
# new_lst = list(set(new_lst))
print(new_lst)


# empty_dict = {}
#
# for num in test_lst:
#     empty_dict[num] = test_lst.count(num)
#
# result = []
# for key in empty_dict.keys():
#     if empty_dict[key] == max(empty_dict.values()):
#         result.append(key)
#
# print(result)