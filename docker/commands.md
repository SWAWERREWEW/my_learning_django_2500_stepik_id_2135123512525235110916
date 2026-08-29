docker/commands.md

# Создание образа
## -t = запуск с возможностью работы с терминалом
```shell
docker build . -t first_image:0.2
docker build first_flask_image -t first_flask_image:first_flask_image
```

# Создание и запуск контейнера
## -i = запуск в режиме просмотра логов контейнера
## -t = запуск с возможностью работы с терминалом
## --rm = запуск одноразового контейнера
## -d = запуск в фоновом режиме
## --network имя_сети = запуск в указанной сети
## -e = дополнительные параметры
## -p адрес:host:docker = запуск и подключение к порту docker через порт host
## -P = запуск с автоматическим назначением порта
## -v ${PWD}/folder_from_computer/:/folder_from_container = запуск вместе с созданием тома
## -v name_tom:/folder_from_container = запуск вместе с созданием тома
## -v /folder_from_container = запуск вместе с созданием тома
## --link имя_контейнера:имя_базы_данных = создание соединения с базой данных другого контейнера
(в данном случае запуск одноразового контейнера --rm) <br>
```shell
docker run --rm -it --name first_container first_image:0.2
docker run --rm -d --name postgres_container --network dbnet -e POSTGRES_DB=mydb -e POSTGRES_PASSWORD=1234 -e POSTGRES_USER=postgres -v posgtres_tom:/var/lib/posgresql/data postgres:18-alpine
docker run --rm -d --network dbnet -p 8000:4000 --link postgres_container:dbps --name flask_site_container -v ${PWD}/flask_db_image/flask_project/:/app flask_db_image:flask_db_image
```

# Просмотр запущенных контейнеров (выход ctrl + c)
docker stats

# Просмотр логов запущенного контейнера в реальном времени
docker logs first_container

# Запуск
### -i = вывод в консоль
docker start -i first_container

# Использование команды в работающем контейнере
## -t = запуск с возможностью работы с терминалом
## -i = режим вывода в консоль
## bash = позволяет зайти в контейнер под root
## psql -U имя_пользователя = вход в консоль СУБД posgtres
```shell
docker exec first_container pip install matplotlib
docker exec -it first_container bash
docker exec -it postgres_container psql -U postgres
Выход \q
```

# Просмотр контейнеров
### -a = Все (даже неактивные)
### -q = только идентификаторы
### -f = фильтр с условиями
#### -f status=exited завершённые
#### -f status=running работающие
#### -f status=created новорождённые контейнеры, но не были ни разу запущенны
#### -f status=restarting перезапущенные
#### -f exited=130 с кодом 130
docker ps -a


# Просмотр образов
### -q = отображение только идентификаторов
### -f = отображение только идентификаторов
#### -f dangling=true отображение только неиспользуемых образов
docker images

# Удаление образа
docker rmi first_image

# Удаление контейнера
## -f = предварительная остановка работы контейнера
## -v = параллельное удаление связанного тома
docker rm first_container

# Просмотр связок портов локальной сети и сети docker
docker port first_container

# Тома
## ls = просмотр томов
## rm имя_тома = удаление тома
## inspect имя_тома = подробности тома
## create имя_тома = создание тома
docker volume

# Сети docker
## ls = просмотрв списка сетей
## create имя_сети = создание новой сети
## delete имя_сети = удаление сети
docker network

# Установка образа с dockerhub
https://hub.docker.com/_/postgres
```shell
docker pull postgres:18-alpine
```
