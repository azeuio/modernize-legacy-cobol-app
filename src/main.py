from operations import op_credit, op_debit, op_total
from data import DataProgram
from IOHandler import ConsoleIOHandler, BaseIOHandler

def handle_user_choice(user_choice: str, data: DataProgram, io_handler: BaseIOHandler) -> bool:
    """
    Handles the user's menu choice and performs the corresponding operation.

    Parameters:
        user_choice (str): The user's selected menu option.
        data (DataProgram): The data handler for reading and writing balance information.
        io_handler (BaseIOHandler): The input/output handler for user interaction.

    Returns:
        bool: True to continue the program loop, False to exit.

    Operations:
        '1' - Display total balance.
        '2' - Perform a credit operation and update balance.
        '3' - Perform a debit operation and update balance.
        '4' - Exit the program.
        Any other input - Display an invalid choice message.

    Exceptions:
        ValueError - Continues the program if an invalid amount is entered.
        EOFError - Handles input closure gracefully.
    """
    try:
        match user_choice.strip().upper():
            case '1':
                op_total(data, io_handler)
            case '2':
                final_balance = op_credit(data, io_handler)
                data.write(final_balance)
            case '3':
                final_balance = op_debit(data, io_handler)
                data.write(final_balance)
            case '4':
                # Exit the program
                return False
            case _:
                # Ignore unknown operation types
                io_handler.display_message(f"Invalid choice ({user_choice}), please select 1-4.")
    except ValueError:
        # Just continue the program on invalid amount error
        return True
    except EOFError:
        # New line to have a good display even on input closing
        io_handler.display_message("")
    return True


def main(io_handler: BaseIOHandler):
    """Main function to run the balance management program."""
    try:
        running = True
        data = DataProgram()
        while running:
            io_handler.display_menu()
            user_choice = io_handler.get_user_input("Enter your choice (1-4): ")

            running = handle_user_choice(user_choice, data, io_handler)
    except EOFError:
        # Gracefully exit on closing input
        pass

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main(ConsoleIOHandler())