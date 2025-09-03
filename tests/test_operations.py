import pytest
from math import isnan
from src.operations import op_total, op_credit, op_debit
from src.data import BaseDataProgram
from src.IOHandler import BaseIOHandler

class MockDataProgram(BaseDataProgram):
    def __init__(self, initial_balance=0.0):
        self._storage_balance = initial_balance

    def read(self):
        return self._storage_balance

    def write(self, balance: float):
        self._storage_balance = balance
        return self._storage_balance
    
class MockIOHandler(BaseIOHandler):
    def __init__(self, user_inputs=""):
        super().__init__()
        self.user_inputs = user_inputs.splitlines()
        self.input_index = 0

    def display_menu(self):
        pass

    def get_user_input(self, _prompt: str):
        if self.input_index < len(self.user_inputs):
            user_input = self.user_inputs[self.input_index]
            self.input_index += 1
            return user_input
        raise EOFError("No more input available.")

    def display_message(self, message: str):
        print(message)

def test_op_total_no_changes():
    assert op_total(MockDataProgram(100), MockIOHandler()) == 100, "Total should not change upon viewing it"
    assert op_total(MockDataProgram(1.2), MockIOHandler()) == 1.2, "Total should not change upon viewing it"
    assert op_total(MockDataProgram(-1.2), MockIOHandler()) == -1.2, "Total should not change upon viewing it"
    assert op_total(MockDataProgram(float('Inf')), MockIOHandler()) == float('Inf'), "Total should not change upon viewing it"
    assert op_total(MockDataProgram(-float('Inf')), MockIOHandler()) == -float('Inf'), "Total should not change upon viewing it"
    assert isnan(op_total(MockDataProgram(float('Nan')), MockIOHandler())), "Total should not change upon viewing it"

def test_op_credit_adds_amount():
    assert op_credit(MockDataProgram(100), MockIOHandler("50")) == 150
    assert op_credit(MockDataProgram(0), MockIOHandler("0")) == 0
    assert op_credit(MockDataProgram(-10), MockIOHandler("10")) == 0
    assert op_credit(MockDataProgram(1.5), MockIOHandler("2.5")) == 4.0

def test_op_credit_invalid_amount():
    with pytest.raises(ValueError):
        op_credit(MockDataProgram(100), MockIOHandler("abc"))
        assert False, "Should raise ValueError"

def test_op_credit_large_numbers():
    assert op_credit(MockDataProgram(0), MockIOHandler(str(5_000_000_000_000_000))) == 5_000_000_000_000_000, (
        "python handles infinitly large numbers. As such, there is no reason to limit number size. "
        "The test value is quadrillion, the value of earth according to Gregory Laughlin(2020). "
        "It is also about 12000 times the net worth of the richest man on earth(2025) and is thus, not expect to be handled"
    )

def test_op_debit_subtracts_amount():
    assert op_debit(MockDataProgram(100), MockIOHandler("50")) == 50
    assert op_debit(MockDataProgram(10), MockIOHandler("10")) == 0
    assert op_debit(MockDataProgram(5.5), MockIOHandler("2.5")) == 3.0

def test_op_debit_insufficient_funds():
    # Balance should not change with insufficient funds
    assert op_debit(MockDataProgram(10), MockIOHandler("20")) == 10
    assert op_debit(MockDataProgram(0), MockIOHandler("1")) == 0

def test_op_debit_invalid_amount():
    with pytest.raises(ValueError):
        op_debit(MockDataProgram(100), MockIOHandler("xyz"))
        assert False, "Should raise ValueError"

def test_intentional_bug_op_credit_negative_treated_as_positive():
    assert op_credit(MockDataProgram(100), MockIOHandler("-12")) == 112, (
    "This bug (negative number treated as positive) "
    "has been here long enough that people might depend on it."
    )

def test_intentional_bug_op_debit_negative_treated_as_positive():
    assert op_debit(MockDataProgram(100), MockIOHandler("-12")) == 88, (
    "This bug (negative number treated as positive) "
    "has been here long enough that people might depend on it."
    )