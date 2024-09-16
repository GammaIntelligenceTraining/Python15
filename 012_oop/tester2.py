class Employee:

    # CLASS VARIABLES
    raise_amount = 1.04

    def __init__(self, name, surname, salary):
        self.name = name.title()
        self.surname = surname.title()
        self.salary = float(salary)
        self.email = f'{name.lower()}.{surname.lower()}@company.com'

    def fullname(self):
        return f'{self.name.title()} {self.surname.title()}'

    def raise_salary(self):
        self.salary *= self.raise_amount


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, name, surname, salary, prog_lang):
        # Employee.__init__(self, name, surname, salary)
        super().__init__(name, surname, salary)
        self.prog_lang = prog_lang

    def work(self):
        return f'{self.fullname()} is writing {self.prog_lang} code!'


class Manager(Employee):

    def __init__(self, name, surname, salary, employees=None):
        super().__init__(name, surname, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


emp1 = Employee('Jack', 'Smith', 2000)
dev1 = Developer('Sarah', 'Gold', 3000, 'python')
man1 = Manager('Bob', 'Summer', 4000, [emp1, dev1])

# print(isinstance(man1, Developer))
print(issubclass(Manager, Developer))