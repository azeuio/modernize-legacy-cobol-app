from src.data import DataProgram

def test_starting_money():
    """Test for starting money"""
    data = DataProgram()
    assert data.read() == 1000, "Starting balance should be 1000.0"

def test_read_write_money():
    """Test for reading and writing money"""
    data = DataProgram()
    data.write(500)
    assert data.read() == 500, "Balance should be 500.0"