import requests
from environs import Env

from terminaltables import AsciiTable


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
    title = 'SuperJob Moscow'
    table_instance = AsciiTable(table_data, title)
    return table_instance.table


if __name__ == '__main__':
    env = Env()
    env.read_env()
    sj_key = env.str('SJ_KEY')
    url = 'https://api.superjob.ru/2.0/vacancies/'
    languages = [
        'JavaScript', 'Java', 'Python',
        'Ruby', 'PHP', 'C++',
        'C#', 'C', 'Go'
        ]
    town_id = '1'
    category = 48
    vacancies_on_page = 20
    average_salary = {}
    for language in languages:
        page = 0
        pages_number = 1
        all_vacancies = []
        while page < pages_number:
            headers = {'X-Api-App-Id': sj_key}
            params = {
                'town': town_id, 'catalogues': category,
                'keyword': f'{language}', 'page': page
            }
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            vacancies = response.json()
            average_salary[f'{language}'] = {
                'vacancies_found': vacancies['total']
            }
            all_vacancies.extend(vacancies['objects'])
            pages_number = round(vacancies['total'] / vacancies_on_page)
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
        else:
            average_salary[f'{language}']['average_salary'] = 0

    print(make_table(average_salary))
