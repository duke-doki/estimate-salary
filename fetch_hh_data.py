from time import sleep

import requests
from terminaltables import AsciiTable


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


def make_table(data):
    table_data = [
        [
            'Язык программирования', 'Вакансий найдено',
            'Вакансий обработано', 'Средняя зарплата'
        ]
    ]
    for language in data:
        table_data.append(
            [
                language, data[language]['vacancies_found'],
                data[language]['vacancies_processed'],
                data[language]['average_salary']
            ]
        )
    # pprint.pprint(average_salary)
    title = 'HeadHunter Moscow'
    table_instance = AsciiTable(table_data, title)
    return table_instance.table


if __name__ == '__main__':
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
                vacancy_salary = predict_rub_salary(vacancy)
                if vacancy_salary:
                    vacancies_processed.append(vacancy_salary)

        average_salary = {
            f'{language}': {'vacancies_found': vacancies['found'],
                            'vacancies_processed': len(vacancies_processed),
                            'average_salary': int(sum(vacancies_processed)
                                                  / len(vacancies_processed))
                            }
        }
        all_languages.update(average_salary)
        sleep(sec_timeout)
    print(make_table(all_languages))
