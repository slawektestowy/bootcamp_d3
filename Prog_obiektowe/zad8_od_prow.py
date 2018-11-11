# 1. zaimportowac klasę CashMachine
# 2. stworzyć podklasę CashMachinePremium
# 3. Zdefiniować wyjątki:
#     StackError (za dużo banknotów)
#     WrongAmountError (kwota nie dzieli sie przez 50)
#     EmptyMachineError (nie da sie zrealizowac kwoty dostepnymi banknotami)
# 4. przetestowac CashMachinePremium
#       cmp ma rzucac wyjatki (raise)
#       pytest ma te wyjatki lapac
# 5. dodac interfejs tekstowy (w osobnym pliku)
#     obslugujacy wyjatki rzucane przez CashMachinePremium
#       dopiero tu beda try-except
import pytest
from zadanie5 import CashMachine

class StackError(Exception):
    pass
class WrongAmountError(Exception):
    pass
class EmptyMachineError(Exception):
    pass

class CashMachinePremium(CashMachine):
    def __init__(self,max_load):
        super().__init__()
        self.max_load = max_load
    def put_money(self, new_banknotes):
        if len(self._banknotes) + len(new_banknotes) > self.max_load:
            raise StackError
        super().put_money(new_banknotes)

def test_new_CashMachinePremium():
    cm = CashMachinePremium(20) # maksymalna pojemnosc kasetki
    assert not cm.is_available  # jest pusty

def test_to_many_banknotes():
    cm = CashMachinePremium(5)
    with pytest.raises(StackError):
        cm.put_money([200,100,100,50,50,50]) # za dużo banknotów
#
# def test_wrong_amount():
#     cm = CashMachinePremium(20)
#     with pytest.raises(WrongAmountError):
#         cm.withdraw_money(130) # kwota nie dzieli się przez 50
#
# def test_wrong_amount2():
#     cm = CashMachinePremium(20)
#     cm.put_money([200, 100, 100, 50, 50, 50])
#     with pytest.raises(WrongAmountError):
#         cm.withdraw_money(123) # kwota nie dzieli się przez 50
#
# def test_bad_banknotes():
#     cm = CashMachinePremium(20)
#     cm.put_money([200, 200, 200])
#     with pytest.raises(EmptyMachineError):
#         cm.withdraw_money(150) # kwota nie da sie zrealizowac dostępnymi banknotami