class User:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f'姓名:{self.name}')
        print(f'薪資:{self.salary}')

u1 = User('A','28900')
u1.show()

class Designer(User):
    def __init__(self, name, salary, job):
        super().__init__(name, salary)
        self.job = job
    def show(self):
        print(f'姓名:{self.name}')
        print(f'薪資:{self.salary}')
        print(f'職稱:{self.job}')

class Designer2(User):
    def __init__(self, name, salary, job):
        self.name=name
        self.salary=salary
        self.job=job
    def show(self):
        print(f'姓名:{self.name}')
        print(f'職稱:{self.job}')
#
# d1 = Designer('AA','28900','平面設計師')
d1 = Designer('AA','28900')
d1.show()
#
# d2 = Designer2('BB','28900','平面設計師')
# d2.show()