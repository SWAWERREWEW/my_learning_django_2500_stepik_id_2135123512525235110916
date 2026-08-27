docker/commands.md

# Создание образа
docker build . -t first_image:0.2

# Создание контейнера
docker run -it --name first_container first_image:0.2

# Запуск
docker start -i first_container
