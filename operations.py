# TODO: replace with actual implementation
def data_program(mode, balance):
    # Fonction factice pour simuler l'appel à 'DataProgram'
    if mode == 'READ':
        return balance
    elif mode == 'WRITE':
        return balance

def op_total():
    final_balance = data_program('READ', final_balance)
    print(f"Current balance: {final_balance:.2f}")

def op_credit():
    
    amount_str = input("Enter credit amount: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount.")
        return
    final_balance = data_program('READ', final_balance)
    final_balance += amount
    data_program('WRITE', final_balance)
    print(f"Amount credited. New balance: {final_balance:.2f}")

def op_debit():
    amount_str = input("Enter debit amount: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount.")
        return
    final_balance = data_program('READ', final_balance)
    if final_balance >= amount:
        final_balance -= amount
        data_program('WRITE', final_balance)
        print(f"Amount debited. New balance: {final_balance:.2f}")
    else:
        print("Insufficient funds")

def operations(passed_operation):
    operation_type = passed_operation.strip().upper()
    final_balance = 1000.00

    match operation_type:
        case 'TOTAL':
            pass
        case 'CREDIT':
            pass
        case 'DEBIT':
            pass
        case _:
            # Ignore unknown operation types
            return False

    return True
