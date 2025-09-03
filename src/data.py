class BaseDataProgram: # pragma: no cover
    def read(self):
        raise NotImplementedError

    def write(self, balance: float):
        raise NotImplementedError

class DataProgram(BaseDataProgram):
    def __init__(self):
        self._storage_balance = 1000.00  # Initial balance

    def read(self):
        return self._storage_balance

    def write(self, balance: float):
        self._storage_balance = balance
        return self._storage_balance
