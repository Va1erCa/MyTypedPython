# Собственное исключение при ошибке ввода координат
class IncorrectCoordinateInput(Exception):
    """Program can't get current GPS coordinates"""
    ...


class ApiServiceError(Exception):
    """Program get API-service error"""
    ...
