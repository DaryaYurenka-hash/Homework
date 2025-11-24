# Установка через командную строку
# pip install pyowm

# если venv
# pip install --upgrade setuptools


# from pyowm import OWM
# from pprint import pprint (красивенько печатает)

# OWM 
# owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
# mgr = owm.weather_manager()


# # print(dir(str))
# # print(dir(mgr))

# Прогноз погоды по местоположению,
# переводим переменную в словарь с помощью to_dict
# w = mgr.weather_at_place('Minsk')
# ww = w.to_dict()

# Использовать pprint(), чтобы вывело красиво) 
# pprint(ww)
# pprint(ww['weather']['wind']['speed'])