# Zaimplementuj klase CashMachine umozliwiajaca wpłacanie i
# wypłacanie pieniedzy. Zadbaj o to aby stan bankomatu
# przetrzymywany był w zmiennych prywatnych.
# Przykład uzycia:
# >>> cash_machine = CashMachine()
# >>> cash_machine.is_available()
# False
# >>> cash_machine.put_money([200, 100, 100, 50])
# >>> cash_machine.is_available()
# True
# >>> cash_machine.withdraw_money(150)
# [100, 50]

class CashMachine():
    def __init__(self):
        self._banknotes = []

    @property
    def is_available(self):
        return bool(self._banknotes)

    def put_money(self, new_banknotes):
        self._banknotes.extend(new_banknotes)
        self._banknotes.sort(reverse=True)

    def withdraw_money(self, amount):
        to_withdraw = []
        for b in self._banknotes:
            if b <= amount:
                to_withdraw.append(b)
                amount -= b
        if amount == 0:
            for b in to_withdraw:
                self._banknotes.remove(b)
            return to_withdraw
        else:
            return []


def test_new_cash_machine():
    cash_machine = CashMachine()
    assert not cash_machine.is_available


def test_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available

def test_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    cash = cash_machine.withdraw_money(150)
    cash.sort(reverse=True)
    assert cash == [100,50]

def test_fail_withdrawal():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    cash = cash_machine.withdraw_money(170)
    cash.sort(reverse=True)
    assert cash == []

def test_two_ways_withdrawal():
    cash_machine = CashMachine()
    cash_machine.put_money([100, 100,  50])
    cash = cash_machine.withdraw_money(250)
    cash.sort(reverse=True)
    assert cash == [200, 50] or (cash == [100,100,50])

# trudniejsza wersja - praca domowa (dla chętnych)
def test_withdraw_money_premium():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50, 20, 20, 20])
    cash = cash_machine.withdraw_money(160)
    cash.sort(reverse=True)
    assert cash == [100,20,20,20]