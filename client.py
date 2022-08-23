# Тестовое задание Teachbase (Python)
# 1. Client для работы с Teachbase API.
#   a. Авторизация.
#   b. Проверка токена.
#   c. Отправка запросов.

import os
import requests
from config import AUTHORIZATION_URL, API_URL


PUB_KEY = os.getenv('PUB_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')


class TeachbaseClient:
    def __init__(self, api_url, authorization_url):
        self.api_url = api_url
        self.authorization_url = authorization_url
        self.token = None
        self.token_type = None

    def authorize(self, client_id, client_secret):
        """
        Gets access token
        """
        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }
        response = requests.post(self.authorization_url, json=data).json()
        # print(json.dumps(response, indent=4))
        self.token = response['access_token']
        self.token_type = response['token_type']

    def get_courses(self):
        return requests.get(self.api_url + '/courses',
                            headers={'Authorization': f'{self.token_type} {self.token}'}).json()

    def get_course(self, course_id):
        return requests.get(self.api_url + '/courses/' + str(course_id),
                            headers={'Authorization': f'{self.token_type} {self.token}'}).json()


if __name__ == '__main__':
    client = TeachbaseClient(API_URL, AUTHORIZATION_URL)
    client.authorize(PUB_KEY, SECRET_KEY)
    courses = client.get_courses()
    print("courses:", courses)
    course = client.get_course(55894)
    print("course 55894:", course)