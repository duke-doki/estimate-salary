import pprint

import requests
from environs import Env


def predict_rub_salary_for_superJob(vacancy):
    if vacancy['currency'] == 'rub':
        if not vacancy['payment_from'] and not vacancy['payment_to']:
            return None
        elif not vacancy['payment_from']:
            return vacancy['payment_to'] * 0.8
        elif not vacancy['payment_to']:
            return vacancy['payment_from'] * 1.2
        else:
            return (vacancy['payment_from'] + vacancy['payment_to']) / 2
    else:
        return None


if __name__ == '__main__':
    env = Env()
    env.read_env()
    sj_token = env.str('SJ_TOKEN')
    url = 'https://api.superjob.ru/2.0/vacancies/'
    languages = [
        'JavaScript', 'Java', 'Python',
        'Ruby', 'PHP', 'C++',
        'C#', 'C', 'Go'
        ]

    average_salary = {}
    for language in languages:
        page = 0
        pages_number = 1
        all_vacancies = []
        while page < pages_number:
            headers = {'X-Api-App-Id': sj_token}
            params = {
                'town': 4, 'catalogues': 48,
                'keyword': f'{language}', 'page': page
            }
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            vacancies = response.json()
            average_salary[f'{language}'] = {
                'vacancies_found': vacancies['total']
            }
            all_vacancies.extend(vacancies['objects'])
            pages_number = round(vacancies['total'] / 20)
            page += 1

        vacancies_processed = []
        for vacancy in all_vacancies:
            vacancy_salary = predict_rub_salary_for_superJob(vacancy)
            if vacancy_salary:
                vacancies_processed.append(vacancy_salary)

        average_salary[f'{language}']['vacancies_processed'] = (
            len(vacancies_processed)
        )

        if len(vacancies_processed):
            average_salary[f'{language}']['average_salary'] = (
                int(sum(vacancies_processed) / len(vacancies_processed))
            )

    pprint.pprint(average_salary)
