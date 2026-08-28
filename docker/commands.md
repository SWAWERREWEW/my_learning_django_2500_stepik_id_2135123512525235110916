docker/commands.md

# Создание образа
## -t = Откладывание яйца
docker build . -t first_image:0.2
docker build first_flask_image -t first_flask_image:first_flask_image

# Создание и запуск контейнера
## -i = запуск в режиме просмотра логов контейнера
## -t = Откладывание яйца
## --rm = запуск одноразового контейнера
## -d = запуск в фоновом режиме
## -p адрес:host:docker = запуск и подключение к порту docker через порт host
## -P = запуск с автоматическим назначением порта
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
## -t = Откладывание яйца
## -i = режим вывода в консоль
## bash = позволяет зайти в контейнер под root
docker exec first_container pip install matplotlib
docker exec -it first_container bash

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

# Просмотр связок портов локальной сети и сети docker
docker port first_container
