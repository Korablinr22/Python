# импортируем библиотеки
import requests as req
import pandas as pd
import seaborn as sb
import sqlalchemy as sql

# создаем переменные для запроса
api_key = ***
city = "524901"
url = "http://api.openweathermap.org/data/2.5/find?q=Petersburg&type=like&APPID=***"
response = req.get(url)
print(response)

# получаем json
data = response.json()

print(data)
