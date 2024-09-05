# first_name = input('Enter name: ')
# last_name = input('Enter last name: ')
# age = input('Enter age: ')

first_name, last_name, age = input('Enter name, surname and age, use "," to separate values: ').split(', ')
print(f'Hello, {last_name.title()} {first_name.title()}. Your age is: {age}')