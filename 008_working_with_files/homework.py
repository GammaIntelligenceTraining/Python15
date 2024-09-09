import string
path = 'text_files/trimushketera.txt'
# ПРИМЕР БЕЗ БИБЛИОТЕКИ STRING
# with open(path, 'r', encoding='utf8') as file:
#     data = file.read()
#     data = data.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('\n', ' ')
#     words = data.split()
#     unique = list(set(words))
#     unique.sort()

# ПРИМЕР С БИБЛИОТЕКОЙ STRING
with open(path, 'r', encoding='utf8') as file:
    data = file.read().lower()
    for char in string.punctuation:
        data = data.replace(char, '')
    words = data.split()
    unique = list(set(words))
    unique.sort()

with open('text_files/trimushketera_copy.txt', 'w', encoding='utf8') as file:
    file.write(f'There are {len(words)} words\n')
    file.write(f'There are {len(unique)} unique words\n')
    for word in unique:
        file.write(f'{word}\n')
