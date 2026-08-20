# my_learning_django_2500_stepik_id_2135123512525235110916

# Изучаемый курс
https://stepik.org/lesson/1089289/step/1?auth=login&unit=1099867

### Подготовка секретов
Нужно создать файл <br>
sitewomen\.env
<br>
и прописать в нем переменные окружения <br>
IP=***
<br>
EMAIL_HOST_PASSWORD=***пароль_от_почтовой_программы
<br>
EMAIL_HOST_USER=***Почта_с_настройками_почтовой_программой
<br>
SECRET_KEY=***секретный_ключ_django
<br>
SOCIAL_AUTH_GITHUB_KEY=***публичный_ключ_приложения_на_github
<br>
SOCIAL_AUTH_GITHUB_SECRET=***секретный_ключ_приложения_на_github
<br>
SOCIAL_AUTH_VK_OAUTH2_KEY=***id_приложения_на_vk
<br>
SOCIAL_AUTH_VK_OAUTH2_SECRET=***защищённый_ключ_приложения_на_github

### Подготовка данных
Нужно переместить папку media и базу данных db.sqlite3 в папку sitewomen
Прописать в настройках либо базу данных по умолчанию
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
либо PostgreSQL
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

### Подготовка домена
Нужно в файл <br>
C:\Windows\System32\drives\etc\hosts
<br>
Добавить строку <br>
127.0.0.1 sitewomen.ru

### Подготовка виртуального окружения и технологий
python -m venv .venv
<br>
.\.venv\Scripts\activate.bat
<br>
pip install -r req.txt
<br>
pip list

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
python -Xutf8 manage.py dumpdata --indent=2 -o women/fixtures/db.json

### Загрузка данных в базу данных из json файла
python manage.py loaddata women/fixtures/db.json

# Прочее
    # Удаление файлов и папки из отслеживаемых
    git rm --cached .idea/vcs.xml
    <br>
    git rm --cached .idea/my_learning_django_2500_stepik_id_2135123512525235110916.iml
    <br>
    git rm --cached .idea/misc.xml
    <br>
    git rm -r --cached .idea

    # откатить коммит, сохранив изменения в индексе
    git reset --soft HEAD~1

    # убрать файл из индекса
    git reset HEAD sitewomen\sitewomen\settings.py

    # создать новый коммит с тем же сообщением
    git commit -c ORIG_HEAD

    # выход из окна редактирования
    :wq

    # отправка на github
    git push origin main --force
