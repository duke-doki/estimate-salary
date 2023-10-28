from time import sleep

import requests

from fetch_data_helper import make_table, predict_rub_salary_for_headhunter


def fetch_hh_data():
    title = 'HeadHunter Moscow'
    url = 'https://api.hh.ru/vacancies'
    languages = [
        'JavaScript', 'Java', 'Python',
        'Ruby', 'PHP', 'C++',
        'C#', 'C', 'Go'
    ]
    town_id = '1'
    amount_of_days = '30'
    sec_timeout = 30
    all_languages = {}
    for language in languages:
        page = 0
        pages_number = 1
        all_vacancies = []
        while page < pages_number:
            params = {
                'area': town_id, 'period': amount_of_days,
                'text': f'программист {language}', 'page': page
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            vacancies = response.json()

            all_vacancies.extend(vacancies['items'])
            pages_number = vacancies['pages']
            page += 1

        vacancies_processed = []
        for vacancy in all_vacancies:
            if vacancy['salary']:
                vacancy_salary = predict_rub_salary_for_headhunter(vacancy['salary'])
                if vacancy_salary:
                    vacancies_processed.append(vacancy_salary)

        if vacancies_processed:
            all_languages[language] = {
                'vacancies_found': vacancies['found'],
                'vacancies_processed': len(vacancies_processed),
                'average_salary': int(sum(vacancies_processed)
                                      / len(vacancies_processed))
            }

        sleep(sec_timeout)
    print(make_table(all_languages, title))


if __name__ == '__main__':
    fetch_hh_data()
