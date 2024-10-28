# Модуль конфигурации применения координат: точные/примерные

# Флаг точного/приблизительного применения координат (False/True)
USE_ROUNDED_COORDS = False

# Координаты по умолчанию
LATITUDE = 48.403121
LONGITUDE = 40.280044

# Шаблоны для доступа к API сервиса OpenWeather
OPENWEATHER_API = "3915122e704b3f5950da77e4959343bc"
OPENWEATHER_URL = (
"https://api.openweathermap.org/data/2.5/weather?"
"lat={latitude}&lon={longitude}&"
"appid=" + OPENWEATHER_API + "&lang=ru&"
"units=metric"
)
