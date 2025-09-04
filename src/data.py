class BaseDataProgram: # pragma: no cover
    """Abstract base class for the data storage."""
    def read(self):
        """Reads the current balance."""
        raise NotImplementedError

    def write(self, balance: float):
        """Writes the new balance."""
        raise NotImplementedError

class DataProgram(BaseDataProgram):
    """Simple, local storage for user's balance"""
    def __init__(self):
        self._storage_balance = 1000.00  # Initial balance

    def read(self):
        return self._storage_balance

    def write(self, balance: float):
        self._storage_balance = balance
        return self._storage_balance
