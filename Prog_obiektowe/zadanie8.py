import pytest

from zadanie5 import CashMachine


class StackError(Exception):
    pass


class CashMachinePremium(CashMachine):
    pass


def test_new_CashMachinePremium():
    cm = CashMachinePremium(20)
    assert not cm.is_available == False




def test_to_many_banknotes():
    cm = CashMachinePremium(5)
    with pytest.raises(StackError):
        cm.put_money([200,100,100,50,50,50])