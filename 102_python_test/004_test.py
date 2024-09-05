user_list = input('Please enter list elements separated with ",": ').split(', ')

for item in user_list[::-1]:
    print(item)