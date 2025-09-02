from main import handle_user_choice

def mock_callable(s: str):
    print(s)

def test_exit():
    assert handle_user_choice(mock_callable, '4') == False, "4 is the exit option and thus should return False to quit"

def test_continue():
    assert handle_user_choice(mock_callable, '1') == True, "1 is not the exit option and thus should return True"
    assert handle_user_choice(mock_callable, '2') == True, "2 is not the exit option and thus should return True"
    assert handle_user_choice(mock_callable, '3') == True, "3 is not the exit option and thus should return True"
    
    assert handle_user_choice(mock_callable, '3') == True, "-1 is not the exit option and thus should return True"
    assert handle_user_choice(mock_callable, '3') == True, "5 is not the exit option and thus should return True"
    assert handle_user_choice(mock_callable, float('Inf')) == True, "Inf is not the exit option and thus should return True"
    assert handle_user_choice(mock_callable, float('-Inf')) == True, "-Inf is not the exit option and thus should return True"
    assert handle_user_choice(mock_callable, float('Nan')) == True, "Nan is not the exit option and thus should return True"
