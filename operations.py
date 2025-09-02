from data import DataProgram
from exceptions import InvalidAmountError

def op_total(data: DataProgram) -> float:
    final_balance = data.read()
    print(f"Current balance: {final_balance:.2f}")
    return final_balance

def op_credit(data: DataProgram, amount_str: str) -> float:
    final_balance = data.read()
    try:
        amount = abs(float(amount_str))
    except ValueError:
        print(f"Invalid amount. Balance: {final_balance: .2f}")
        raise InvalidAmountError
    final_balance += amount
    data.write(final_balance)
    print(f"Amount credited. New balance: {final_balance:.2f}")
    return final_balance

def op_debit(data: DataProgram, amount_str: str) -> float:
    final_balance = data.read()
    try:
        amount = abs(float(amount_str))
    except ValueError:
        print(f"Invalid amount. Balance: {final_balance: .2f}")
        raise InvalidAmountError
    if final_balance >= amount:
        final_balance -= amount
        data.write(final_balance)
        print(f"Amount debited. New balance: {final_balance:.2f}")
    else:
        print(f"Insufficient funds. Balance: {final_balance: .2f}")
    return final_balance
