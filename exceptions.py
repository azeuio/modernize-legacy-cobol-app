class InvalidAmountError(RuntimeError):
    def __init__(self, message="Le montant saisi n'est pas valide."):
        super().__init__(message)