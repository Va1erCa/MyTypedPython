# imports from our modules
from exceptions import ApiServiceError, IncorrectCoordinateInput
from gps_coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather


def main():
    try:
        coordinates = get_gps_coordinates()
    except IncorrectCoordinateInput:
        print('Не правильно введены GPS координаты!')
        exit(1)
    try:
        # weather = get_weather(coordinates)
        weather = get_weather(coordinates)
    except ApiServiceError:
        print('Не смог получить погоду по API сервиса!')
        exit(1)
    print(format_weather(weather))


if __name__ == '__main__':
    main()
