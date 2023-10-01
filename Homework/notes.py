
class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_employee_info(self):
        return f'{self.name}, {self.age} years old'


class Engineer(Employee):
    
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang

class Manager(Employee):

    def __init__(self, name, age, dep, employees=None):
        super().__init__(name, age)
        self.dep = dep
        if employees is not None:
            self.employees = employees
        else:
            self.employees = []

    def get_manager_info(self):
        return f"{self.name}, {self. age} years old, manager of {self.dep}"

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_emp(self, employees):
        if employees in self.employees:
            self.employees.remove(employees)

    def print_emp(self):
        for emp in self.employees:
            print(emp.get_employee_info())

eng1 = Engineer("Ed", 27, "Python")
eng2 = Engineer("Vasya", 44, "C++")
man1 = Manager("Josh", 40, "Web", [eng1, eng2])

print(man1.get_employee_info())
print(man1.get_manager_info())
man1.print_emp()