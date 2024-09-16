import re
text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
12312-123-123123123
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr.Thomas
abc
example*company
-
hall, ball, mall, wall, tall

ööbik
привет
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'\b\d{3}[-.]\d{3}[-.]\d{3,4}\b')

# pattern = re.compile(r'M(r|s|rs)\.? ?[A-Z][a-z]*')

# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


# with open('people.txt', 'r', encoding='utf8') as file:
#     data = file.read()
#     pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
#     matches = pattern.finditer(data)
#     for m in matches:
#         print(m.span())

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov.uk
https://example.net
www.example.net
example.net
admin.123shop.com.
'''

# pattern = re.compile(r'(https?://)?(www\.)?([a-zA-Z0-9-]+)([.a-zA-Z0-9-]+)')
#
# matches = pattern.finditer(urls)
# for m in matches:
#     print(m.group())

pattern = re.compile(r'\w+', re.VERBOSE)
# matches = pattern.split('Hello. My name is Jack! How old are you?')
matches = pattern.findall(text_to_search)
# for m in matches:
#     print(m.group())
print(matches)