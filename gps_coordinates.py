# Модуль получения координат

from dataclasses import dataclass
import config
from exceptions import IncorrectCoordinateInput
from coordinates import Coordinates

def get_gps_coordinates() -> Coordinates:
    """

    :rtype: object
    """
    # Получаем широту
    print('Введите широту,')
    latitude = _get_coord(90, config.LATITUDE)
    # Получаем долготу
    print('Введите долготу, ')
    longitude = _get_coord(180, config.LONGITUDE)
    return _round_coordinates(Coordinates(latitude=latitude, longitude=longitude))

def _get_coord(border: int, default: float) -> float:
    coordinate = default
    print(f'введите значение в формате [[+/-]##[.######]] в диапазоне от -{border} до +{border}:')
    string_input = input().strip()
    if len(string_input) == 0:
        print(f'Выбрано значение по-умолчанию: {default}')
    else:
        try:
            coordinate = float(string_input)
        except ValueError:
            print('Ошибка: введено не число.')
            raise IncorrectCoordinateInput
        if coordinate < -border or coordinate > border:
            raise IncorrectCoordinateInput
    return coordinate

def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    # округляем если задано в настройках
    if config.USE_ROUNDED_COORDS:
        return Coordinates(*map(lambda c: round(c, 1), [coordinates.longitude, coordinates.longitude]))
    else:
        return coordinates

if __name__ == "__main__":
    print(get_gps_coordinates())