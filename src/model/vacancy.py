class Vacancy:
    name: str
    salary: float
    url: str
    requirements: str
    responsibility: str

    def __init__(self, name, salary, url, requirement, responsibility):
        self.name = name
        self.salary = salary
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
