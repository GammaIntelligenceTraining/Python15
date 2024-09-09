# 'r' - read
# 'w' - write
# 'a' - append
# 'x' - create
# 'r+' - read and write

# file = open(r'text_files\test.txt', 'r', encoding='utf8')
#
# print(file.encoding)
# print(file.mode)
# print(file.closed)
# file.close()
# print(file.closed)

# with open(r'text_files\test.txt', 'r', encoding='utf8') as file:
#     data = file.read()
#
# data = data.lower()
# with open(r'text_files\test_copy.txt', 'w', encoding='utf8') as file2:
#     file2.write(data)

# with open('text_files/python.jpg', 'rb') as file:
#     with open('text_files/python_copy.jpg', 'wb') as file2:
#         data = file.read(20096)
#         file2.write(data)
path = r'text_files/trimushketera.txt'
with open(path, 'r', encoding='utf8') as file:
    data = file.read()
    print(data)
