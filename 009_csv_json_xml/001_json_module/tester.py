import json
# data = '''{
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false,
#       "salary": 1500
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true,
#       "salary": 1700
#     },
#     {
#       "name": "Steven Cooke",
#       "phone": null,
#       "emails": "stevencooke@example.com",
#       "has_licence": true,
#       "salary": 2500
#     }
#   ]
# }'''
#
# people = json.loads(data)
# print(people)
# print(type(people))
# print(json.dumps([], indent=4))

with open('data.json', 'r', encoding='utf8') as file:
    people = json.load(file)
    print(people)

for person in people['people']:
    if not person['has_licence']:
        people['people'].remove(person)

with open('data2.json', 'w', encoding='utf8') as file:
    json.dump(people, file, indent=4)
