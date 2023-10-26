# Programming vacancies compare

This project helps to find vacancies for most popular programming languages, 
representing a convenient table.

### fetch_hh_data.py

To see data from [HeadHunter](https://hh.ru/) run:
```
python fetch_hh_data.py
```

### fetch_sj_data.py

For this you need to put a secret key `SJ_KEY` inside `.env` file, 
which can be accessed [here](https://api.superjob.ru/info/).

To see data from [SuperJob](https://www.superjob.ru/) run:
```
python fetch_sj_data.py
```


### How to install

For scripts to work run:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).