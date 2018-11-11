# Zaimplementuj klase PremiumEmployee, która bedzie klasa
# pochodna Employee. Klasa ta powinna umozliwiac dodatkowo
# przyznawanie bonusów pracownikowi.
#   employee = PremiumEmployee('Jan', 'Nowak', 100.0)
#
#
#     >> employee.register_time(5)
#
#     >> employee.give_bonus(1000.0)
#
#     >> employee.pay_salary()
#
#   1500.0





from zadanie2 import Employee


class PremiumEmployee(Employee):
    def __init__(self, fname, sname, rate):
        super().__init__(fname,sname,rate)
        self.bonus = 0


    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        return Employee.pay_salary(self) + self.bonus

def test_new_employee():
    em = PremiumEmployee('Jan', 'Nowak', 100.0)
    assert em.fname == 'Jan'
    assert em.sname == 'Nowak'
    assert em.rate == 100.0

def test_regular_time():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500


def test_bonus():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000.0)
    assert employee.pay_salary() == 1500.0

def test_double_bonus():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000)
    assert employee.pay_salary() == 1500
    employee.register_time(5)
    employee.give_bonus(1000)
    assert employee.pay_salary() == 1500