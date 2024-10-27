# Модуль получения координат

from dataclasses import dataclass
from exception import IncorrectCoordinateInput

# применяем slots и frozen для преобразования к компактному хранению и если нужен read only объект
# @dataclass(slots=True, frozen=True)
@dataclass()         #  без slots и frozen - not read only object
class Coordinates:
    longitude: float
    latitude: float
def get_gps_coordinates() -> Coordinates:
    # Координаты по умолчанию: 48.403121, 40.280044
    coords = Coordinates(longitude=48.403121, latitude=40.280044)

    print('Введите широту в формате [[+/-]##[.######]] в диапазоне от -90 до +90:')
    string_inp = input().strip()
    if len(string_inp) == 0:
        print('Выбрано значение широты по-умолчанию: 48.403121')
    else:
        try:
            coords.latitude = float(string_inp)
        except ValueError:
            print('Введено не число.')
            raise IncorrectCoordinateInput
        if coords.latitude < -90 or coords.latitude > 90:
            raise IncorrectCoordinateInput

    print('Введите долготу в формате [##[.######]] в диапазоне от -180 до +180:')
    string_inp = input().strip()
    if len(string_inp) == 0:
        print('Выбрано значение долготы по-умолчанию: 40.280044')
    else:
        try:
            coords.longitude = float(string_inp)
        except ValueError:
            print('Введено не число.')
            raise IncorrectCoordinateInput
        if coords.longitude < -180 or coords.longitude > 180:
            raise IncorrectCoordinateInput

    return coords

if __name__ == "__main__":
    print(get_gps_coordinates())