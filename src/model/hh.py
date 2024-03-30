import json

import requests

from src.model.AbstractAPI import AbstractAPI


class HH(AbstractAPI):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def get_vacancies(self, keyword):
        pass

    def save_to_file(self, file_name):
        pass

    def add_vacancy(self, vacancy):
        pass

    def filter_vacancies(self, criteria):
        pass

    def remove_vacancy(self, vacancy):
        pass
