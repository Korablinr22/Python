# импортируем библиотеки
import requests as req
import pandas as pd
import seaborn as sb
import sqlalchemy as sql

# создаем переменные для запроса
 создаем переменные для запроса
api_key = 'cf4d1efcc9b3ee304ac0562d0359b27a'
city = 'Biysk'
url = f'http://api.openweathermap.org/data/2.5/find?q={city}&type=like&APPID={api_key}'
response = req.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    print(f'Соединение установлено, код ответа: {response.status_code}')
else:
    print(f'Что-то пошло не так, код ошибки: {response.status_code}')

print(response)

# получаем json
data = response.json()

print(data)
