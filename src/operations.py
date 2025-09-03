from IOHandler import BaseIOHandler
from data import DataProgram

def op_total(data: DataProgram, io_handler: BaseIOHandler) -> float:
    final_balance = data.read()
    io_handler.display_message(f"Current balance: {final_balance:.2f}")
    return final_balance

def op_credit(data: DataProgram, io_handler: BaseIOHandler) -> float:
    amount_str = io_handler.get_user_input("Enter amount to credit: ")
    final_balance = data.read()
    try:
        amount = abs(float(amount_str))
    except ValueError:
        io_handler.display_message(f"Invalid amount. Balance: {final_balance: .2f}")
        raise ValueError
    final_balance += amount
    data.write(final_balance)
    io_handler.display_message(f"Amount credited. New balance: {final_balance:.2f}")
    return final_balance

def op_debit(data: DataProgram, io_handler: BaseIOHandler) -> float:
    amount_str = io_handler.get_user_input("Enter amount to debit: ")
    final_balance = data.read()
    try:
        amount = abs(float(amount_str))
    except ValueError:
        io_handler.display_message(f"Invalid amount. Balance: {final_balance: .2f}")
        raise ValueError
    if final_balance >= amount:
        final_balance -= amount
        data.write(final_balance)
        io_handler.display_message(f"Amount debited. New balance: {final_balance:.2f}")
    else:
        io_handler.display_message(f"Insufficient funds. Balance: {final_balance: .2f}")
    return final_balance
