from typing import Callable
from operations import operations

def handle_user_choice(operations: Callable[[str], None], user_choice: str) -> bool:
    if user_choice == '4':
        return False
    if user_choice == '1':
        operations('TOTAL')
    elif user_choice == '2':
        operations('CREDIT')
    elif user_choice == '3':
        operations('DEBIT')
    else:
        print("Invalid choice, please select 1-4.")
    return True

def run(get_user_choice: Callable[[], str]) -> bool:
    """"""
    print("--------------------------------")
    print("Account Management System")
    print("1. View Balance")
    print("2. Credit Account")
    print("3. Debit Account")
    print("4. Exit")
    print("--------------------------------")
    user_choice = get_user_choice()

    return handle_user_choice(operations, user_choice)

def main():
    
    try:
        while run(lambda: input("Enter your choice (1-4): ")):
            pass
    except EOFError:
        # Gracefully exit on closing input
        pass

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()