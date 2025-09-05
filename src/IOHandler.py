class BaseIOHandler:
    """Abstract base class for IO Handlers."""
    def display_menu(self):
        """Displays the menu to the user."""
        raise NotImplementedError

    def get_user_input(self):
        """Gets input from the user."""
        raise NotImplementedError

    def display_message(self, _message: str):
        """Displays a message to the user."""
        raise NotImplementedError
    
    def amount_repr(self, amount: float):
        """Displays an amount to the user."""
        return f"{amount:09.2f}"

# Not included in coverage because it is not part of the core logic
class ConsoleIOHandler(BaseIOHandler): # pragma: no cover
    """Concrete IO Handler that interacts via the console."""
    def display_menu(self):
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")

    def get_user_input(self, prompt: str):
        return input(prompt + "\n")

    def display_message(self, message: str):
        print(message)