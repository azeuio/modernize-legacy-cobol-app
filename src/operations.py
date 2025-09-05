from math import isnan, isinf
from IOHandler import BaseIOHandler
from data import DataProgram

def op_total(data: DataProgram, io_handler: BaseIOHandler) -> float:
    """Displays the total balance."""
    final_balance = data.read()
    io_handler.display_message(f"Current balance: {io_handler.amount_repr(final_balance)}")
    return final_balance

def op_credit(data: DataProgram, io_handler: BaseIOHandler) -> float:
    """
    Performs a credit operation (adds funds).
    
    Exceptions:
        ValueError - Raised if the input amount is invalid.
    """
    amount_str = io_handler.get_user_input("Enter amount to credit: ")
    final_balance = data.read()
    try:
        amount = abs(float(amount_str))
        if isnan(amount) or isinf(amount):
            raise ValueError
    except ValueError:
        io_handler.display_message(f"Invalid amount. Balance: {io_handler.amount_repr(final_balance)}")
        raise ValueError
    final_balance += amount
    data.write(final_balance)
    io_handler.display_message(f"Amount credited. New balance: {io_handler.amount_repr(final_balance)}")
    return final_balance

def op_debit(data: DataProgram, io_handler: BaseIOHandler) -> float:
    """
    Performs a debit operation (subtracts funds).
    Exceptions:
        ValueError - Raised if the input amount is invalid.
    """
    amount_str = io_handler.get_user_input("Enter amount to debit: ")
    final_balance = data.read()
    try:
        amount = abs(float(amount_str))
        if isnan(amount) or isinf(amount):
            raise ValueError
    except ValueError:
        io_handler.display_message(f"Invalid amount. Balance: {io_handler.amount_repr(final_balance)}")
        raise ValueError
    if final_balance >= amount:
        final_balance -= amount
        data.write(final_balance)
        io_handler.display_message(f"Amount debited. New balance: {io_handler.amount_repr(final_balance)}")
    else:
        io_handler.display_message(f"Insufficient funds. Balance: {io_handler.amount_repr(final_balance)}")
    return final_balance
