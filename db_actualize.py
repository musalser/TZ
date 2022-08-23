# Тестовое задание Teachbase (Python)
# 3. Сохранение данных из Teachbase (*).



from client import TeachbaseClient
import sqlite3
import os
import requests
from config import AUTHORIZATION_URL, API_URL, LOACAL_API_URL

# Ключи для авторизации в TeachBase храним в переменных окружения
PUB_KEY = os.getenv('PUB_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

# Коннект к нашей базе
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# Получаем курсы из TeachBase
client = TeachbaseClient(API_URL, AUTHORIZATION_URL)
client.authorize(PUB_KEY, SECRET_KEY)
tb_courses = client.get_courses()

# Сохраняем отсутствующие курсы
for tb_course in tb_courses:
    cur.execute(f"SELECT id FROM tz_course WHERE id = {tb_course['id']}")
    found = cur.fetchall()
    if not found:
        r = requests.post(LOACAL_API_URL + '/courses/', json=tb_course)
con.close()
