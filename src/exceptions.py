class ZeroQuantityProduct(Exception):  # новые ошибки наследуются от класса Exception
    def __init__(self, message=None):
        super().__init__(message)
