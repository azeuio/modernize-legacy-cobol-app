from main import handle_user_choice
from data import BaseDataProgram
from IOHandler import BaseIOHandler

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

    def get_user_input(self):
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
