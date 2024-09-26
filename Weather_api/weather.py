# импортируем библиотеки
import requests as req
import pandas as pd
import seaborn as sb
import sqlalchemy as sql

# создаем переменные для запроса
api_key = '***'
city = 'Biysk'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = req.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    print(f'Соединение установлено, код ответа: {response.status_code}')
else:
    print(f'Что-то пошло не так, код ошибки: {response.status_code}')

# получаем json
data = response.json()

print(data)
