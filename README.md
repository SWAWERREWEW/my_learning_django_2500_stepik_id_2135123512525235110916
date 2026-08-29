# my_learning_django_2500_stepik_id_2135123512525235110916

# Изучаемый курс
https://stepik.org/lesson/1089289/step/1?auth=login&unit=1099867

### Подготовка секретов
Нужно создать файл <br>
sitewomen\.env
и прописать в нем переменные окружения
```
IP=***
EMAIL_HOST_PASSWORD=***пароль_от_почтовой_программы
EMAIL_HOST_USER=***Почта_с_настройками_почтовой_программой
SECRET_KEY=***секретный_ключ_django
SOCIAL_AUTH_GITHUB_KEY=***публичный_ключ_приложения_на_github
SOCIAL_AUTH_GITHUB_SECRET=***секретный_ключ_приложения_на_github
SOCIAL_AUTH_VK_OAUTH2_KEY=***id_приложения_на_vk
SOCIAL_AUTH_VK_OAUTH2_SECRET=***защищённый_ключ_приложения_на_github
```

### Подготовка данных
Нужно переместить папку media и базу данных db.sqlite3 в папку sitewomen
Прописать в настройках либо базу данных по умолчанию <br>
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
либо PostgreSQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sitewomen_db',
        'USER': 'sitewomen_user',
        'PASSWORD': PASSWORD_DB,
        'HOST': 'localhost',
        'PORT': 5433,
    }
}
```

### Подготовка домена
Нужно в файл <br>
C:\Windows\System32\drives\etc\hosts
<br>
Добавить строку <br>
127.0.0.1 sitewomen.ru

### Подготовка виртуального окружения и технологий
```
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r req.txt
pip list
```

### Подготовка работы хеширования сайта
win
cmd
Запуск от имени администратора <br>
wsl --install
<br> Перезапуск компьютера Должно появиться окно с консолью. В новой консоли
запустить консоль можно с помощью win wsl после ввода новых имени и пароля нужны команды (Скопированный текст команд
вставляется с помощью правой кнопки мыши)
    
    1. Скачиваем официальный GPG-ключ Redis
    curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
    
    2. Добавляем официальный репозиторий (исправленная версия)
    echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
    
    3. Обновляем списки пакетов и устанавливаем Redis
    sudo apt-get update
    sudo apt-get install redis -y
    
    4. Запускаем службу
    sudo service redis-server start
    
    Для проверки (Слово PONG в выводе означает успех)
    redis-cli
    ping
    Для выхода нужны клавишы ctrl + c
    
    5. Остановка сервера
    sudo service redis-server stop
    
    (Удаление wsl и Redis при необходимости)

    sudo service redis-server stop
    sudo apt-get purge redis redis-server -y
    sudo apt-get autoremove -y
    sudo rm /etc/apt/sources.list.d/redis.list
    sudo rm /usr/share/keyrings/redis-archive-keyring.gpg
    Можно посмотреть имя установленной системы (обычно там написано Ubuntu) (Внимание: это мгновенно и безвозвратно удалит Linux, Redis и все файлы внутри WSL).:
    wsl --list
    Удалить её командой:
    wsl --unregister Ubuntu


### Запуск
cd sitewomen
<br>
python manage.py runserver

### Обновление базы данных или создание пустой
python manage.py makemigrations
<br>
python manage.py migrate

### Запуск с доступом для других устройств в локальной сети
python manage.py runserver 0.0.0.0:8000

### Запуск с протоколом https
python manage.py runserver_plus --cert-file cert.crt

### Выгрузка данных в json файл
```
python -Xutf8 manage.py dumpdata --indent=2 -o women/fixtures/db.json
python -Xutf8 manage.py dumpdata --indent=2 women.Women -o women/fixtures/women_women.json
python -Xutf8 manage.py dumpdata --indent=2 women.Category -o women/fixtures/women_category.json
python -Xutf8 manage.py dumpdata --indent=2 women.TagPost -o women/fixtures/women_tagpost.json
python -Xutf8 manage.py dumpdata --indent=2 women.Husband -o women/fixtures/women_husband.json
```

### Загрузка данных в базу данных из json файла
python manage.py loaddata women/fixtures/db.json

## Просле завершения разработки включить кеш
```
cmd
wsl
sudo service redis-server start
redis-cli
ping
```

### Очистка кеша
FLUSHDB

# Запуск на сервере
    Команды для обновления системы и установки базовых технологий для django
    sudo apt update
    sudo apt install python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib nginx
    sudo apt install build-essential libpython3-dev gunicorn
    
    Запуск консоли Postgre
    sudo -u postgres psql
    
    Создание базы данных
    CREATE DATABASE sitewomen_db;
    CREATE USER sitewomen WITH PASSWORD '12345678';
    
    Потом настройки созданного пользователя
    ALTER ROLE sitewomen SET client_encoding TO 'utf8';
    ALTER ROLE sitewomen SET default_transaction_isolation TO 'read committed';
    ALTER ROLE sitewomen SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE sitewomen_db TO sitewomen;
    ALTER DATABASE sitewomen_db OWNER TO sitewomen;
    
    Выход из консоли Postgre
    \q
    
    Создание виртуального окружения в выбранной папке
    cd /var/www
    mkdir sitewomen_project
    
    Существует способ автоматически создать файл со списком всех зависимостей из виртуального окружения
    pip freeze > req.txt
    
    В файле не должно быть библиотек (если они есть, нужно их убрать)
    certifi==2023.7.22
    cffi==1.15.1
    psycopg2==2.9.7
    
    Нужно загрузить все файлы проекта (кроме папки .djvenv) на удалённый сервер.
    Это можно сделать с помощью кнопки 'Загрузить файлы', а создание виртуального окружения реализуется обычными командами
    python3 --version
    Активация виртуального окружения происходит другой командой
    source djvenv/bin/activate
    Отключение или деактивация
    deactivate

    nano sitewomen\sitewomen\settings.py
    ...
    import os
    ...
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'sitewomen.ru', 'ip_адрес_сервера', 'домен', 'www.домен']
    # INTERNAL_IPS = ["127.0.0.1"]
    ...
    Debug=False
    ...
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'sitewomen_db',
            'USER': 'sitewomen_user',
            'PASSWORD': '12345678',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ...
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    # STATICFILES_DIRS (закомментировать)

    sudo apt install ufw
    sudo ufw allow 8000

    Открытие сайта по адресу
    http://домен:8000
    Либо
    http://ip_адрес_сервера:8000
    
    Передача
    scp -P [порт] -r \путь\к\папке\сайта\на\ПК root_или_имя_пользователя@[IP_сервера]:/путь/к/my_project/на/сервере
    Пример
    scp -P 50067 "D:\python\my_django\sitewomen\women\fixtures\db.json" kikidon@192.168.5.55:/home/kikidon/my_django/sitewomen/women/fixtures/
    
    📝📦📥📊
    Заполнение базы данных
    python3 sitewomen/manage.py loaddata db.json

    nano /etc/systemd/system/gunicorn.service
    🛠📝📦
    И записать в него
    [Unit]
    Description=gunicorn daemon
    After=network.target
    
    [Service]
    User=kikidon
    Group=www-data
    WorkingDirectory=/home/kikidon/learn
    ExecStart=/home/kikidon/my_django/.venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/kikidon/my_django/sitewomen.sock sitewomen.wsgi:application
    Restart=on-failure
    
    [Install]
    WantedBy=multi-user.target

    Запуск gunicorn
    sudo systemctl enable --now gunicorn
    После запуска появится файл
    /home/kikidon/my_django/sitewomen.sock
    
    Проверка
    sudo systemctl status gunicorn
    
    Настройка nginx
    Нужно создать файл
    nano /etc/nginx/sites-available/myproject
    🛠📝📦
    И записать в него
    server {
        listen 80;
        server_name домен.ru *.домен.ru;
    
        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ { root /home/kikidon/my_django; }
        location /media/ { root /home/kikodon/my_django; }
    
        location / {
            include proxy_params;
            proxy_pass http://unix:/home/kikidon/my_django/sitewomen.sock;
        }
    }
    
    Нужно создать также ярлык
    sudo ln -s /etc/nginx/sites-available/my_django /etc/nginx/sites-enabled
    
    Проверка на синтаксические ошибки
    sudo nginx -t
    
    Перезапуск nginx и gunicorn
    sudo systemctl restart nginx
    sudo systemctl restart gunicorn
    
    Потом нужно заменить отслеживание порта 8000 на отслеживание nginx
    sudo ufw delete allow 8000
    sudo ufw allow 'Nginx Full'
    
    Осталось настроить права доступа к папкам static и media
    sudo chmod 755 /home/kikidon/my_django/static
    sudo chmod 755 /home/kikidon/my_django/media
    
    Сайт можно открыть по адресу без ":8000"
    http://ip_адрес_сервера
    http://домен


# Запуск на сервере по https
    Сертификат для https либо платный, либо на 90 дней на
    https://letsencrypt.org/ru/
    Для автообновления сертификата была создана программа
    https://certbot.eff.org/pages/about
    
    Установка программы для автообновления сертификата для https
    sudo apt install certbot python3-certbot-nginx -y
    
    Можно получить сертификат для домена по команде, указав почту (настоящую) и согласившись с условиями
    certbot --nginx -d домен.ru
    
    Сертификат создан и активирован, но без автообновления
    Запуск автообновления с помощью работы демона ☠🥀
    certbot --nginx -d домен.ru
    
    Проверка
    systemctl status certbot.timer
    
    Тест автообновления сертификата
    certbot renew --dry-run
    
    
# Прочее
    Удаление файлов и папки из отслеживаемых
    git rm --cached .idea/vcs.xml

    git rm --cached .idea/my_learning_django_2500_stepik_id_2135123512525235110916.iml

    git rm --cached .idea/misc.xml
    
    git rm --cached sitewomen\db.json

    git rm -r --cached .idea

    откатить коммит, сохранив изменения в индексе
    git reset --soft HEAD~1

    убрать файл из индекса
    git reset HEAD sitewomen\sitewomen\settings.py
    git reset HEAD sitewomen\db.json

    создать новый коммит с тем же сообщением
    git commit -c ORIG_HEAD

    выход из окна редактирования
    :wq

    отправка на github
    git push origin main --force
