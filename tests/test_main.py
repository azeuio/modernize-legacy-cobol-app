import pytest
from src.main import handle_user_choice, main
from src.data import BaseDataProgram
from src.IOHandler import BaseIOHandler

# Mocking DataProgram so in the future, if an external DB is used, tests won't be affected
class MockDataProgram(BaseDataProgram):
    def __init__(self):
        self._storage_balance = 1000.00  # Initial balance

    def read(self):
        return self._storage_balance

    def write(self, balance: float):
        self._storage_balance = balance
        return self._storage_balance
    
class MockIOHandler(BaseIOHandler):
    def __init__(self, user_inputs=""):
        super().__init__()
        self.user_inputs = user_inputs.splitlines()
        self.input_index = 0

    def display_menu(self):
        pass

    def get_user_input(self, _prompt: str):
        if self.input_index < len(self.user_inputs):
            user_input = self.user_inputs[self.input_index]
            self.input_index += 1
            return user_input
        raise EOFError("No more input available.")

    def display_message(self, _message: str):
        pass

def test_exit():
    assert handle_user_choice('4', MockDataProgram(), MockIOHandler()) == False, "4 is the exit option and thus should return False to quit"

def test_continue():
    assert handle_user_choice('1', MockDataProgram(), MockIOHandler()) == True, "1 is not the exit option and thus should return True"
    assert handle_user_choice('2', MockDataProgram(), MockIOHandler()) == True, "2 is not the exit option and thus should return True"
    assert handle_user_choice('3', MockDataProgram(), MockIOHandler()) == True, "3 is not the exit option and thus should return True"
    
    assert handle_user_choice('3', MockDataProgram(), MockIOHandler()) == True, "-1 is not the exit option and thus should return True"
    assert handle_user_choice('3', MockDataProgram(), MockIOHandler()) == True, "5 is not the exit option and thus should return True"
    assert handle_user_choice('Inf', MockDataProgram(), MockIOHandler()) == True, "Inf is not the exit option and thus should return True"
    assert handle_user_choice('-Inf', MockDataProgram(), MockIOHandler()) == True, "-Inf is not the exit option and thus should return True"
    assert handle_user_choice('Nan', MockDataProgram(), MockIOHandler()) == True, "Nan is not the exit option and thus should return True"

    assert handle_user_choice('2', MockDataProgram(), MockIOHandler("abc")) == True, "Invalid input should not exit the program"

class MockIntegrationIOHandler(BaseIOHandler):
    def __init__(self, user_inputs=""):
        super().__init__()
        self.user_inputs = user_inputs.splitlines()
        self.input_index = 0

    def display_menu(self):
        print("menu")

    def get_user_input(self, _prompt: str):
        print("prompt")
        if self.input_index < len(self.user_inputs):
            user_input = self.user_inputs[self.input_index]
            self.input_index += 1
            return user_input
        raise EOFError("No more input available.")

    def display_message(self, message: str):
        print(message)

def test_integration(capsys):
    assert main(MockIntegrationIOHandler(
        "1\n" # View balance, should be 1000
        "500\n" # Invalid choice
        "2\n" # Credit an amount
        "1000\n" # Valid credit
        "3\n" # Debit an amount
        "2000\n" # Valid debit
        "4\n" # Exit
        ""
    )) == None, "Integration test failed"
    captured = capsys.readouterr()
    print(captured.out)
    got = captured.out.splitlines()
    assert got[0] == "menu" # initial
    assert got[1] == "prompt"
    assert "1000" in got[2] # display balance
    assert got[3] == "menu" # automaticly back to menu
    assert got[4] == "prompt"
    assert "invalid" in got[5].lower() # invalid choice
    assert got[6] == "menu" # automaticly back to menu
    assert got[7] == "prompt"


def test_integration_eof_quitting(capsys):
    assert main(MockIntegrationIOHandler(
        "1" # View balance, should be 1000
        "" # EOF (should quit)
    )) == None, "Integration test failed"
    captured = capsys.readouterr()
    print(captured.out)
    got = captured.out.splitlines()
    assert got[0] == "menu"
    assert got[1] == "prompt"
    assert "1000" in got[2]
    assert got[3] == "menu"
    assert got[4] == "prompt"
    assert "exiting" in got[5].lower()

def test_integration_eof_back_to_menu(capsys):
    assert main(MockIntegrationIOHandler(
        "2" # Credit an amount
        "" # EOF (should go back to menu, then quit)
    )) == None, "Integration test failed"
    captured = capsys.readouterr()
    print(captured.out)
    got = captured.out.splitlines()
    assert got[0] == "menu"
    assert got[1] == "prompt"
    assert got[2] == "prompt"
    assert got[3] == "" # to have a good looking output
    assert got[4] == "menu"
    assert got[5] == "prompt"
    assert "exiting" in got[6].lower()
    