from typing import Callable
from operations import op_credit, op_debit, op_total, InvalidAmountError
from data import DataProgram
from IOHandler import ConsoleIOHandler, BaseIOHandler

def handle_user_choice(user_choice: str, data: DataProgram, io_handler: BaseIOHandler) -> bool:

    try:
        match user_choice.strip().upper():
            case '1':
                op_total(data)
            case '2':
                final_balance = op_credit(data, io_handler.get_user_input())
                data.write(final_balance)
            case '3':
                final_balance = op_debit(data, io_handler.get_user_input())
                data.write(final_balance)
            case '4':
                # Exit the program
                return False
            case _:
                # Ignore unknown operation types
                io_handler.display_message("Invalid choice, please select 1-4.")
    except InvalidAmountError:
        # Just continue the program on invalid amount error
        return True
    except EOFError:
        # New line to have a good display even on input closing
        io_handler.display_message("")
    return True


def main():
    io_handler = ConsoleIOHandler()
    try:
        running = True
        while running:
            
            data = DataProgram()
            io_handler.display_menu()
            user_choice = io_handler.get_user_input()

            running = handle_user_choice(user_choice, data, io_handler)
    except EOFError:
        # Gracefully exit on closing input
        pass

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()