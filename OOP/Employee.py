class  Employee():

    'Employee类，所有类的基类'

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{}-{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amout):
        cls.raise_amt = amout

# print(Employee.__doc__)
# print('raise_amt=',Employee.raise_amt)
# print('nuum_of_emps=',Employee.num_of_emps)
# print("----------------------")
#
# emp_1 = Employee('corey', 'schafer', 5000)
# emp_2 = Employee('Test', 'User', 6000)
# Employee.set_raise_amt(1.05)
#
# print('raise_amt=',Employee.raise_amt)
# print('nuum_of_emps=',Employee.num_of_emps)

class Developer(Employee):
    raise_amt = 2.0

    def __init__(self,first,last,pay,pro_lang):
        super().__init__(first,last,pay)
        self.pro_lang = pro_lang



# dev_1 = Developer('Corey','Schafer',5000,'Python')
# dev_2 = Developer('Test','User',6000,'Java')
#
# print(dev_1.fullname())
# print(dev_1.pro_lang)
# print(dev_2.pro_lang)

class Manager(Employee):

    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp  not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->',emp.fullname())


# mgr_1 = Manager('Sue','Smith',9000,[dev_1,dev_2])
# print(mgr_1.email)
# mgr_1.print_emps()