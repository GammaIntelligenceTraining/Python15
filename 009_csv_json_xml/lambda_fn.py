x = [[2, 6, 1], [7, 3, 8], [1, 2, 3], [3, 9, 4]]

def second_num(x):
    return x[1]

# x.sort(key=second_num)
x.sort(key=lambda x: x[2])
print(x)


y = lambda a, b: a * b
d = lambda: 'Hello world!'

print(y(10, 20))