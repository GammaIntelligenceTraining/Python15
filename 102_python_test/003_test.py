side_a = float(input('Please enter side A: '))
side_b = float(input('Please enter side B: '))
side_c = float(input('Please enter side C: '))

if side_c ** 2 == side_a ** 2 + side_b ** 2:
    print('This is right triangle.')
else:
    print('This is not right triangle.')