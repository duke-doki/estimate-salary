import requests
from environs import Env

from fetch_data_helper import make_table, predict_rub_salary_for_superJob


def fetch_sj_vacancies(key):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    languages = [
        'JavaScript', 'Java', 'Python',
        'Ruby', 'PHP', 'C++',
        'C#', 'C', 'Go'
    ]
    town_id = 4
    category = 48
    vacancies_on_page = 20
    all_languages = {}
    for language in languages:
        page = 0
        pages_number = 1
        all_vacancies = []
        while page < pages_number:
            headers = {'X-Api-App-Id': key}
            params = {
                'town': town_id, 'catalogues': category,
                'keyword': f'{language}', 'page': page
            }
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            vacancies = response.json()

            all_vacancies.extend(vacancies['objects'])
            pages_number = round(vacancies['total'] / vacancies_on_page)
            page += 1

        vacancies_processed = []
        for vacancy in all_vacancies:
            vacancy_salary = predict_rub_salary_for_superJob(vacancy)
            if vacancy_salary:
                vacancies_processed.append(vacancy_salary)

        if vacancies_processed:
            vacancies_amount = len(vacancies_processed),
            average_salary = int(sum(vacancies_processed)
                                  / len(vacancies_processed))
        else:
            vacancies_amount = 0
            average_salary = 0
        all_languages[language] = {
            'vacancies_found': vacancies['total'],
            'vacancies_processed': vacancies_amount,
            'average_salary': average_salary
        }
    return all_languages


if __name__ == '__main__':
    env = Env()
    env.read_env()
    sj_key = env.str('SJ_KEY')
    title = 'SuperJob Moscow'
    print(make_table(fetch_sj_vacancies(sj_key), title))
