# Модуль получения координат

from dataclasses import dataclass
import config
from exception import IncorrectCoordinateInput

# Типизируем получаемые координаты
# применяем slots и frozen для преобразования к компактному хранению и если нужен read only object
# без slots и frozen - not read only object
@dataclass(slots=True, frozen=True)

class Coordinates:
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    # Инициализируем координатами по умолчанию:
    latitude,  longitude = (config.LATITUDE,  config.LONGITUDE)

    # Получаем широту
    print('Введите широту в формате [[+/-]##[.######]] в диапазоне от -90 до +90:')
    string_input = input().strip()
    if len(string_input) == 0:
        print(f'Выбрано значение широты по-умолчанию: {config.LATITUDE}')
    else:
        try:
            latitude = float(string_input)
        except ValueError:
            print('Ошибка: введено не число.')
            raise IncorrectCoordinateInput
        if latitude < -90 or latitude > 90:
            raise IncorrectCoordinateInput

    # Получаем долготу
    print('Введите долготу в формате [##[.######]] в диапазоне от -180 до +180:')
    string_input = input().strip()
    if len(string_input) == 0:
        print(f'Выбрано значение долготы по-умолчанию: {config.LONGITUDE}')
    else:
        try:
            longitude = float(string_input)
        except ValueError:
            print('Ошибка: введено не число.')
            raise IncorrectCoordinateInput
        if longitude < -180 or longitude > 180:
            raise IncorrectCoordinateInput

    # округляем если задано в настройках
    if config.USE_ROUNDED_COORDS:
        latitude, longitude = map(lambda c: round(c, 1), [latitude, longitude])

    return Coordinates(latitude=latitude, longitude=longitude)

if __name__ == "__main__":
    print(get_gps_coordinates())