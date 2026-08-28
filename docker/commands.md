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
### -i = вывод в консоль
docker start -i first_container

# Использование команды в работающем контейнере
docker exec first_container pip install matplotlib

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
docker rm first_container
