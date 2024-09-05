a = (1, 2, 3, 5, 8)
b = (8,2,5)

# a = a[:2] + b + a[2:]
# print(a)

a = list(a)
for element in b[::-1]:
    a.insert(2, element)

a = tuple(a)
print(a)