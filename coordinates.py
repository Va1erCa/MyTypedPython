# модуль типа Coordinates (координаты)

from dataclasses import dataclass

# Типизируем получаемые координаты
# применяем slots и frozen для преобразования к компактному хранению и если нужен read only object
# без slots и frozen - not read only object
@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float