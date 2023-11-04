class InputException(Exception):
    def __int__(self, message):
        super().__init__(message)


class InvalidModeException(Exception):
    pass
