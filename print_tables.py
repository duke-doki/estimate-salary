from environs import Env

from fetch_data_helper import make_table
from fetch_hh_vacancies import fetch_hh_vacancies
from fetch_sj_vacancies import fetch_sj_vacancies


if __name__ == '__main__':
    env = Env()
    env.read_env()
    sj_key = env.str('SJ_KEY')
    headhunter_title = 'HeadHunter Moscow'
    print(make_table(fetch_hh_vacancies(), headhunter_title))
    superjob_title = 'SuperJob Moscow'
    print(make_table(fetch_sj_vacancies(sj_key), superjob_title))
