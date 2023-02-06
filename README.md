<h2 align="center">Food blog</h2>


**Ссылки**:


### Описание проекта:
Блог кулинара с рецептами


### Инструменты разработки

**Стек:**
- Python >= 3.10.4
- Django==4.1.6
- PostreSQL 15

## Разработка

##### 1) Поставить звездочку)

##### 2) Создать папку проекта (например food_blog)

##### 3) Перейти в папку проекта и клонировать репозиторий 

    git clone https://github.com/LiderStar/food_blog.git

##### 4) Создать виртуальное окружение в папке проекта
    
    python -m venv venv
    
##### 5) Активировать виртуальное окружение
    
Linux

        source venv/bin/activate
    
Windows

        ./venv/Scripts/activate

##### 6) Установить зависимости:
#####   6.1) Обновляем менеджер пакетов pip

        python.exe -m pip install --upgrade pip

#####   6.2) Сами зависимости

        pip install -r requirements.txt

##### 7) Установить БД:

        развернуть PostgreSQL -> создать базу blog и пользователя например admin с правами суперпользователя

##### 8) Выполнить restore DB

        в PGadmin выбрать базу blog  и восстановить ее из резервной копии (Backup_DB/blog)

##### 9) В папке проекта создать файл .env
        пописать в нем:
        
        ALLOWED_HOSTS={127.0.0.1}
        NAME={Имя БД пункт 7}
        USER={Пользователь БД пункт 7}
        PASSWORD={Пароль пользователя БД пункт 7}
        HOST={localhost}
        PORT={порт на котором работает БД по умолчанию 5432}
        SECRET_KEY={django secret key}

##### 10) Выполнить команду для выполнения миграций

        python manage.py migrate
    
##### 11) Создать суперпользователя

        python manage.py createsuperuser
    
##### 12) Запустить сервер

        python manage.py runserver

##### 13) Ссылки

     - Сайт http://127.0.0.1:8000/

     - Админ панель http://127.0.0.1:8000/admin

##### 14) Запросы к ORM в среде jupyter
        
      python manage.py shell_plus --notebook

## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2023-present, LiderStar - Volodymir Zybin.


