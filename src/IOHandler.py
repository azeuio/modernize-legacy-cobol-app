class BaseIOHandler:
    def display_menu(self):
        raise NotImplementedError

    def get_user_input(self):
        raise NotImplementedError

    def display_message(self, _message: str):
        raise NotImplementedError

class ConsoleIOHandler(BaseIOHandler):
    def display_menu(self):
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")

    def get_user_input(self, prompt: str):
        return input(prompt)

    def display_message(self, message: str):
        print(message)