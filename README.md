# Programming vacancies compare

This project helps to find vacancies for most popular programming languages, 
representing a convenient table.

### fetch_hh_data.py

To see data from [HeadHunter](https://hh.ru/) run:
```
python fetch_hh_data.py
```

### fetch_sj_data.py

The purpose of `sj_key` is to get access for SuperJob API.
For this you need to put a secret key `SJ_KEY` inside `.env` file, 
which can be accessed [here](https://api.superjob.ru/info/) after creating your app and generating a secret key. 
For more information see [here](https://api.superjob.ru/).

To see data from [SuperJob](https://www.superjob.ru/) run:
```
python fetch_sj_data.py
```

### print_tables.py

To print both tables with data run:
```
python print_tables.py
```

### How to install

For scripts to work run:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).