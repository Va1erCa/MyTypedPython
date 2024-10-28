# Модуль конфигурации

__doc__='''
Модуль конфигурации
Хранение ключа в .env фале переменных среды окружения.
Содержимое файла .env для корректной работы приложения:
    openweathet_api=<Ваш API-ключ доступа к OpenWeatherApi>
    env_example_list=1,2,3,4,5
    env_example_dict=A=Hello,B=Bye bye
'''

import environ

# Флаг точного/приблизительного применения координат (False/True)
USE_ROUNDED_COORDS = False

# Координаты по умолчаниюd
LATITUDE = 48.403121
LONGITUDE = 40.280044

# чтение секретного api-ключа из файла перенменных среды окружения
env = environ.Env()
environ.Env.read_env()
OPENWEATHER_API = env('openweather_api', str)

# Шаблоны для доступа к API сервиса OpenWeather
OPENWEATHER_URL = (
"https://api.openweathermap.org/data/2.5/weather?"
"lat={latitude}&lon={longitude}&"
"appid=" + OPENWEATHER_API + "&lang=ru&"
"units=metric"
)

if __name__ == "__main__":
    # демо учебных переменных
    ENV_EXAMPLE_LIST = env('env_example_list', list)
    EMV_EXAMPLE_DICT = env('env_example_dict', dict)
    print('Пример работы c переменными среды с помощью библиотеки django_environ:')
    print(f'Итоговый запрос к сервису погоды: {OPENWEATHER_URL}')
    print(f'Переменная среды - список: {ENV_EXAMPLE_LIST}')
    print(f'Переменная среды - словарь: {EMV_EXAMPLE_DICT}')
