# Модуль получения погодных данных

from datetime import datetime
from dataclasses import dataclass
import enum
import requests, json
from json.decoder import JSONDecodeError
# import ssl
from typing import Literal

from requests import Response

# import urllib.request
# from urllib.error import URLError

from coordinates import Coordinates
import config
from exceptions import ApiServiceError

Celsius = float


class WeatherType(enum.StrEnum) :
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


@dataclass(slots=True, frozen=True)
class Weather :
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather :
    """Requests weather in OpenWeather API and returns it"""
    openweather_response = _get_openweather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude)
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(latitude: float, longitude: float) -> Response :
    # ssl._create_default_https_context = ssl._create_unverified_context
    # url = config.OPENWEATHER_URL.format(latitude=latitude, longitude=longitude)
    url = config.OPENWEATHER_URL.format(latitude=latitude, longitude=longitude)

    try :
        # return urllib.request.urlopen(url).read()
        return requests.get(url)
    except Exception:
        raise ApiServiceError


def _parse_openweather_response(openweather_response: Response) -> Weather :
    try :
        # openweather_dict = json.loads(openweather_response)
        openweather_dict = openweather_response.json()
    except JSONDecodeError :
        raise ApiServiceError
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, "sunrise"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        # sunset="2024-10-29",                                  # пример ошибки которую найдет mypy
        city=_parse_city(openweather_dict)
    )


def _parse_temperature(openweather_dict: dict) -> Celsius :
    return round(openweather_dict["main"]["temp"])


def _parse_weather_type(openweather_dict: dict) -> WeatherType :
    try :
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError) :
        raise ApiServiceError
    weather_types = {"1" : WeatherType.THUNDERSTORM,
                     "3" : WeatherType.DRIZZLE,
                     "5" : WeatherType.RAIN,
                     "6" : WeatherType.SNOW,
                     "7" : WeatherType.FOG,
                     "800" : WeatherType.CLEAR,
                     "80" : WeatherType.CLOUDS
                     }
    for _id, _weather_type in weather_types.items() :
        if weather_type_id.startswith(_id) :
            return _weather_type
    raise ApiServiceError


def _parse_sun_time(openweather_dict: dict,
                    time: Literal["sunrise"] | Literal["sunset"]) -> datetime :
    return datetime.fromtimestamp(openweather_dict["sys"][time])


def _parse_city(openweather_dict: dict) -> str :
    return openweather_dict["name"]


if __name__ == "__main__" :
    print(get_weather(Coordinates(latitude=config.LATITUDE, longitude=config.LONGITUDE)))
