# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.pay_salary()
# 500.0
# >>> employee.pay_salary()
# 0.0
# >>> employee.register_time(10)
# >>> employee.pay_salary()
# 1200.0

class Employee():
    def __init__(self, fname, sname, rate):
        self.fname = fname
        self.sname = sname
        self.rate = rate
        self.time = 0
        self.overtime = 0

    def register_time(self,hours):
        if hours <= 8:
            self.time += hours
        else:
            self.time += 8
            self.overtime += hours - 8

    def pay_salary(self):
        cash = self.rate * (self.time + 2* self.overtime)
        self.time = 0
        self.overtime = 0
        return cash

kopacz = Employee('Jan','Nowak',100)
kopacz.register_time(5)
print(kopacz.pay_salary())
print(kopacz.pay_salary())
kopacz.register_time(12)
print(kopacz.pay_salary())