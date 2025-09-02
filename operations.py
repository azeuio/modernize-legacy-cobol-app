from typing import Literal, Union
from exceptions import InvalidAmountError

# TODO: replace with actual implementation
def data_program(mode: Union[Literal['READ'], Literal['WRITE']], balance = 0):
    # Fonction factice pour simuler l'appel à 'DataProgram'
    if mode == 'READ':
        return 1000
    elif mode == 'WRITE':
        return balance

def op_total(final_balance: float) -> float:
    final_balance = data_program('READ', final_balance)
    print(f"Current balance: {final_balance:.2f}")
    return final_balance

def op_credit(final_balance: float, amount_str: str) -> float:
    try:
        amount = abs(float(amount_str))
    except ValueError:
        print(f"Invalid amount. Balance: {final_balance: .2f}")
        raise InvalidAmountError
    final_balance = data_program('READ', final_balance)
    final_balance += amount
    data_program('WRITE', final_balance)
    print(f"Amount credited. New balance: {final_balance:.2f}")
    return final_balance

def op_debit(final_balance: float, amount_str: str) -> float:
    try:
        amount = abs(float(amount_str))
    except ValueError:
        print(f"Invalid amount. Balance: {final_balance: .2f}")
        raise InvalidAmountError
    final_balance = data_program('READ', final_balance)
    if final_balance >= amount:
        final_balance -= amount
        data_program('WRITE', final_balance)
        print(f"Amount debited. New balance: {final_balance:.2f}")
    else:
        print(f"Insufficient funds. Balance: {final_balance: .2f}")
    return final_balance

def operations(passed_operation):
    operation_type = passed_operation.strip().upper()
    final_balance = data_program('READ')

    try:
        match operation_type:
            case 'TOTAL':
                final_balance = op_total(final_balance)
            case 'CREDIT':
                final_balance = op_credit(final_balance, input("Enter debit amount: "))
            case 'DEBIT':
                final_balance = op_credit(final_balance, input("Enter debit amount: "))
            case _:
                # Ignore unknown operation types
                return False
    except InvalidAmountError:
        return False
    except EOFError:
        print() # New line to have a good display even on input closing
        return False
    finally:
        return True
