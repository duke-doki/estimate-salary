from terminaltables import AsciiTable


def make_table(languages, title):
    vacancies_table = [
        [
            'Язык программирования', 'Вакансий найдено',
            'Вакансий обработано', 'Средняя зарплата'
        ]
    ]
    for language in languages:
        vacancies_table.append(
            [
                language, languages[language]['vacancies_found'],
                languages[language]['vacancies_processed'],
                languages[language]['average_salary']
            ]
        )
    table_instance = AsciiTable(vacancies_table, title)
    return table_instance.table


def predict_rub_salary_for_headhunter(vacancy):
    if not vacancy['salary']['currency'] == 'RUR':
        return None
    if not vacancy['salary']['from']:
        return vacancy['salary']['to'] * 0.8
    elif not vacancy['salary']['to']:
        return vacancy['salary']['from'] * 1.2
    else:
        return (vacancy['salary']['from'] + vacancy['salary']['to']) / 2


def predict_rub_salary_for_superJob(vacancy):
    if not vacancy['currency'] == 'rub':
        return None
    if not vacancy['payment_from'] and not vacancy['payment_to']:
        return None
    elif not vacancy['payment_from']:
        return vacancy['payment_to'] * 0.8
    elif not vacancy['payment_to']:
        return vacancy['payment_from'] * 1.2
    else:
        return (vacancy['payment_from'] + vacancy['payment_to']) / 2
