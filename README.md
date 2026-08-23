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

# Прочее
    Удаление файлов и папки из отслеживаемых
    git rm --cached .idea/vcs.xml
    <br>
    git rm --cached .idea/my_learning_django_2500_stepik_id_2135123512525235110916.iml
    <br>
    git rm --cached .idea/misc.xml
    <br>
    git rm -r --cached .idea

    откатить коммит, сохранив изменения в индексе
    git reset --soft HEAD~1

    убрать файл из индекса
    git reset HEAD sitewomen\sitewomen\settings.py

    создать новый коммит с тем же сообщением
    git commit -c ORIG_HEAD

    выход из окна редактирования
    :wq

    отправка на github
    git push origin main --force
