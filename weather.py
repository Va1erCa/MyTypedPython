# imports from our modules
from gps_coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather


def main():
    coordinates = get_coordinates()
    weather = get_weather(coordinates)
    print(format_weather(weather))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
