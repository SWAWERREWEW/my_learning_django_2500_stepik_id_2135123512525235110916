docker/commands.md

# Создание образа
docker build . -t first_image:0.2

# Создание и запуск контейнера
## --rm = запуск одноразового контейнера
## -d = запуск в фоновом режиме
(в данном случае запуск одноразового контейнера --rm) <br>
docker run --rm -it --name first_container first_image:0.2

# Просмотр запущенных контейнеров (выход ctrl + c)
docker stats

# Просмотр логов запущенного контейнера в реальном времени
docker logs first_container

# Запуск
docker start -i first_container

# Использование команды в работающем контейнере
docker exec first_container pip install matplotlib

# Просмотр контейнеров
docker ps -a

# Просмотр образов
docker images

# Удаление контейнера
docker rm first_container
