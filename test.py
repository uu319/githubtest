class Employee:
    raise_amount= 2.2
    num_0f_emp= 0
    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first+'.'+last+'@sym.ph'
        Employee.num_0f_emp+=1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay= int(self.pay * Employee.raise_amount)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount= amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay= emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
emp1 = Employee('Van', 'Diongzon', 50000)
emp2 = Employee('Van', 'Diongzon', 50000)
import datetime
my_date= datetime.date(2018, 11, 12)

# print(Employee.is_workday(my_date))

class Developer(Employee):
    raise_amount= 1.10

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self,first, last, pay)
        self.prog_lang= prog_lang

dev= Developer('Van', 'Diongzon', 5000, 'Python')

# print(dev.email)
# print(dev.prog_lang)

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees= employees
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
dev_1= Developer('Plinky', 'Tamb', 40000, 'Java')
dev_2= Developer('Paul', 'Foro', 40000, 'Java')
manager= Manager('Sidney', 'Diongzon', 4000,[dev_1])
manager.add_employee(dev_2)
# manager.add_employee([dev_1])
# manager.add_employee('Kell')

manager.print_emps()
print(manager.email)
