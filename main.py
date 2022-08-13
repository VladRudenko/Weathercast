import requests
import os
from datetime import datetime
from pytz import timezone
from colorama import Fore, init

init(autoreset=True)


def smile(status):
    weather_descript = {
        "Clear": "\U00002600",
        "Clouds": "\U000026C5",
        "Thunderstorm": "\U000026C8",
        "Drizzle": "\U0001F326",
        "Rain": "\U0001F327",
        "Snow": "\U00002744",
        "Mist": "\U0001f32b",
        "Fog": "\U0001f32b",
        "Haze": "\U0001f32b",
        "Tornado": "\U0001f32a"
    }
    if status in weather_descript:
        return weather_descript[status]


while True:
    city = input(Fore.CYAN + "Введите название города/страны : " + Fore.RESET)
    os.system("cls")
    try:
        key = "b9f2f2da9d96e34da1e68b3f6e65b807"
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"APPID": key, "q": city, "units": "metric", "lang": "ru"}
        result = requests.get(url, params=params)
        get_weather = result.json()
        tz_UA = timezone("Europe/Kiev")

        print("*** " + datetime.now(timezone("Europe/Kiev")).strftime(
            "%y-%m-%d/%H:%M:%S" + " ***"))

        print("Страна >>> " + get_weather["sys"]["country"])

        print("Город >>> " + get_weather["name"])

        print("Температура >>> " + str(get_weather["main"]["temp"]) + "°C" +
              ", Ощущается, как >>> " +
              str(get_weather["main"]["feels_like"]) + "°C" +
              ", Мин. темп >>> " + str(get_weather["main"]["temp_min"]) +
              "°C" + ", Макс. темп >>> " +
              str(get_weather["main"]["temp_max"]) + "°C")

        print("Состояние погоды >>> " +
              get_weather["weather"][0]["description"] +
              str(smile(get_weather["weather"][0]["main"])))

        print("Скорость ветра >>> " + str(get_weather["wind"]["speed"]) +
              "м/с")

        print("Влажность >>> " + str(get_weather["main"]["humidity"]) + "%")

        print("Давление >>> " + str(get_weather["main"]["pressure"]) + "мбар")

        print("Время рассвета >>> " + str(
            datetime.fromtimestamp(get_weather["sys"]["sunrise"],
                                   tz_UA).strftime("%y-%m-%d/%H:%M")))

        print("Время заката >>> " + str(
            datetime.fromtimestamp(get_weather["sys"]["sunset"],
                                   tz_UA).strftime("%y-%m-%d/%H:%M")))

        print("Продолжительность часового дня >>> " + str(
            datetime.fromtimestamp(get_weather["sys"]["sunset"]) -
            datetime.fromtimestamp(get_weather["sys"]["sunrise"])))

        print("-" * 40)
    except KeyError:
        print(Fore.RED + "Города/страны под названием : " + Fore.WHITE + city +
              Fore.RED + ", не существует. Повторите попытку\n")
