# import json
# # data = '''{
# #   "people": [
# #     {
# #       "name": "Jack Sumers",
# #       "phone": "555-555-555",
# #       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
# #       "has_licence": false,
# #       "salary": 1500
# #     },
# #     {
# #       "name": "Mary Smith",
# #       "phone": "777-777-777",
# #       "emails": null,
# #       "has_licence": true,
# #       "salary": 1700
# #     },
# #     {
# #       "name": "Steven Cooke",
# #       "phone": null,
# #       "emails": "stevencooke@example.com",
# #       "has_licence": true,
# #       "salary": 2500
# #     }
# #   ]
# # }'''
# #
# # people = json.loads(data)
# # print(people)
# # print(type(people))
# # print(json.dumps([], indent=4))
#
# with open('data.json', 'r', encoding='utf8') as file:
#     people = json.load(file)
#     print(people)
#
# for person in people['people']:
#     if not person['has_licence']:
#         people['people'].remove(person)
#
# with open('data2.json', 'w', encoding='utf8') as file:
#     json.dump(people, file, indent=4)

#
# x = {'name': 'Jack'}
#
# print(x.get('name'))

# x = ['One', 'Two', 'Three']
# y = list(enumerate(x, 1))
# print(y)
# for i in y:
#     print(i)
#
# for i in y:
#     print(i)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(num):
    if num % 2 == 0:
        return True
    return False

for num in filter(lambda num: (num % 2 == 0), x):
    print(num)

def second_value(tup):
    return tup[1]

x = [(3, 5), (1, 4), (6, 3), (9, 2)]
x.sort(key=lambda x: x[1])
print(x)

a = lambda num, name: print(num, name)

a(1, 'hello')
b = lambda: print('Hello world')
b()