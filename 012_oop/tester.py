import datetime
class Employee:

    # CLASS VARIABLES
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, name, surname, salary):
        self.name = name.title()
        self.surname = surname.title()
        self.salary = float(salary)
        self.email = f'{name.lower()}.{surname.lower()}@company.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return f'{self.name.title()} {self.surname.title()}'

    def raise_salary(self):
        self.salary *= self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def emp_from_string(cls, string):
        name, surname, salary = string.split('-')
        return cls(name, surname, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() in [5, 6]:
            return False
        return True


emp1 = Employee('Jack', 'Smith', 2000)
emp2 = Employee.emp_from_string('MARY-GOLD-3000')
print(emp2.fullname())

now = datetime.datetime.today()
print(Employee.is_workday(now))
