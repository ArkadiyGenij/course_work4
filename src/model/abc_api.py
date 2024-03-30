from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        """Метод для получения информации о вакансиях с использованием ключевого слова."""
        pass

    @abstractmethod
    def save_to_file(self, file_name):
        """Метод для сохранения информации о вакансиях в файл."""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии."""
        pass

    @abstractmethod
    def filter_vacancies(self, criteria):
        """Метод для фильтрации вакансий по заданным критериям."""
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy):
        """Метод для удаления вакансии."""
        pass
