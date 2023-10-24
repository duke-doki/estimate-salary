import requests
import pprint
from time import sleep

url = 'https://api.hh.ru/vacancies'

languages = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go']

# vacancies_amount = {}
# for language in languages:
#     params = {'area': '1', 'period': '30', 'text': f'программист {language}'}
#     response = requests.get(url, params=params)
#     response.raise_for_status()
#     vacancies_amount[f'{language}'] = response.json()['found']
#
# pprint.pprint(vacancies_amount)


# params = {'area': '1', 'period': '30', 'text': 'программист python'}
# response = requests.get(url, params=params)
# response.raise_for_status()
#
# vacancies = response.json()


def predict_rub_salary(vacancy):
    if vacancy['salary']['currency'] == 'RUR':
        if not vacancy['salary']['from']:
            return vacancy['salary']['to'] * 0.8
        elif not vacancy['salary']['to']:
            return vacancy['salary']['from'] * 1.2
        else:
            return (vacancy['salary']['from'] + vacancy['salary']['to']) / 2
    else:
        return None


average_salary = {}

for language in languages:
    print(language)
    page = 0
    pages_number = 1
    all_vacancies = []
    while page < pages_number:
        print(page)
        params = {'area': '1', 'period': '30', 'text': f'программист {language}', 'page': page}
        response = requests.get(url, params=params)
        response.raise_for_status()
        vacancies = response.json()
        average_salary[f'{language}'] = {'vacancies_found': vacancies['found']}
        all_vacancies.extend(vacancies['items'])
        pages_number = vacancies['pages']
        page += 1


    vacancies_processed = []
    for vacancy in all_vacancies:
        if vacancy['salary']:
            vacancy_salary = predict_rub_salary(vacancy)
            if vacancy_salary:
                vacancies_processed.append(vacancy_salary)

    average_salary[f'{language}']['vacancies_processed'] = len(vacancies_processed)
    average_salary[f'{language}']['average_salary'] = int(sum(vacancies_processed) / len(vacancies_processed))
    print(f'{language} finished, wait 30 secs')
    sleep(30)

pprint.pprint(average_salary)
