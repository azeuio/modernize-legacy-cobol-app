from operations import op_total, op_credit, op_debit
from exceptions import InvalidAmountError
from math import isnan

def test_op_total_no_changes():
    assert op_total(100) == 100, "Total should not change upon viewing it"
    assert op_total(1.2) == 1.2, "Total should not change upon viewing it"
    assert op_total(-1.2) == -1.2, "Total should not change upon viewing it"
    assert op_total(float('Inf')) == float('Inf'), "Total should not change upon viewing it"
    assert op_total(-float('Inf')) == -float('Inf'), "Total should not change upon viewing it"
    assert isnan(op_total(float('Nan'))), "Total should not change upon viewing it"

def test_op_credit_adds_amount():
    assert op_credit(100, "50") == 150
    assert op_credit(0, "0") == 0
    assert op_credit(-10, "10") == 0
    assert op_credit(1.5, "2.5") == 4.0

def test_op_credit_invalid_amount():
    try:
        op_credit(100, "abc")
        assert False, "Should raise InvalidAmountError"
    except InvalidAmountError:
        return

def test_op_credit_large_numbers():
    assert op_credit(0, str(5_000_000_000_000_000)) == 5_000_000_000_000_000, (
        "python handles infinitly large numbers. As such, there is no reason to limit number size. "
        "The test value is quadrillion, the value of earth according to Gregory Laughlin(2020). "
        "It is also about 12000 times the net worth of the richest man on earth(2025) and is thus, not expect to be handled"
    )

def test_op_debit_subtracts_amount():
    assert op_debit(100, "50") == 50
    assert op_debit(10, "10") == 0
    assert op_debit(5.5, "2.5") == 3.0

def test_op_debit_insufficient_funds():
    # Balance should not change with insufficient funds
    assert op_debit(10, "20") == 10
    assert op_debit(0, "1") == 0

def test_op_debit_invalid_amount():
    try:
        op_debit(100, "xyz")
        assert False, "Should raise InvalidAmountError"
    except InvalidAmountError:
        pass

def test_intentional_bug_op_credit_negative_treated_as_positive():
    assert op_credit(100, "-12") == 112, (
    "This bug (negative number treated as positive) "
    "has been here long enough that people might depend on it."
    )

def test_intentional_bug_op_debit_negative_treated_as_positive():
    assert op_debit(100, "-12") == 88, (
    "This bug (negative number treated as positive) "
    "has been here long enough that people might depend on it."
    )