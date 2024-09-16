class Employee:

    # CLASS VARIABLES
    raise_amount = 1.04

    def __init__(self, name, surname, salary):
        self.name = name.title()
        self.surname = surname.title()
        self.salary = float(salary)
        self.email = f'{name.lower()}.{surname.lower()}@company.com'

    @property
    def fullname(self):
        return f'{self.name.title()} {self.surname.title()}'

    @fullname.setter
    def fullname(self, new_name):
        name, surname = new_name.split()
        self.name = name
        self.surname = surname

    def raise_salary(self):
        self.salary *= self.raise_amount

    def __str__(self):
        return self.fullname()

    def __add__(self, other):
        return self.salary + other.salary


emp1 = Employee('Jack', 'Smith', 2000)
emp2 = Employee('Sarah', 'Gold', 3000)

# import datetime
# now = datetime.datetime.now()
# print(repr(now))
# print(emp1 + emp2)
print(emp1.fullname)
emp1.fullname = 'Bob Summers'
print(emp1.fullname)
print(emp1.name)