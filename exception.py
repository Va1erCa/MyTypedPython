# Собственное исключение при ошибке ввода координат
class IncorrectCoordinateInput(Exception):
    """Program can't get current GPS coordinates"""
    ...