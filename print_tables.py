from environs import Env

from fetch_data_helper import make_table
from fetch_headhunter import fetch_headhunter
from fetch_superjob import fetch_superjob


if __name__ == '__main__':
    env = Env()
    env.read_env()
    sj_key = env.str('SJ_KEY')
    headhunter_title = 'HeadHunter Moscow'
    print(make_table(fetch_headhunter(), headhunter_title))
    superjob_title = 'SuperJob Moscow'
    print(make_table(fetch_superjob(sj_key), superjob_title))
