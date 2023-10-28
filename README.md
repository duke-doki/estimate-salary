# Programming vacancies compare

This project helps to find vacancies for most popular programming languages, 
representing a convenient table.

### fetch_hh_data.py

To see data from [HeadHunter](https://hh.ru/) run:
```
python fetch_hh_data.py
```

### fetch_sj_data.py


For this script to work properly with the API you need to access a secret key after registering your own app 
[here](https://api.superjob.ru/info/). You need to create `.env` file in the same folder with 
`fetch_sj_data.py` and store there `SJ_KEY` which must be equal to your key.


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