# Foodgram - сервис для публикации рецептов
![example workflow](https://github.com/mrvinil/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

Проект Foodgram позволяет пользователям публиковать рецепты, добавлять рецепты в избранное и список покупок, подписыватся на других пользователей и скачивать список продуктов.

### Проект доступен по адрессу:
[walmarkt.ru](http://walmarkt.ru/)

### Доступ в админку для суперюзера:
```bash
login - admin@walmarkt.ru
pass - !passw0rd!
```

### Доступ в ЛК для обычного пользователя:
```bash
login - user@walmarkt.ru
pass - user!passw0rd!
```

### Технологии
- Python
- Django
- Docker
- postgresql
- nginx
- gunicorn

### Запуск проекта на сервере
## Для работы сервиса на сервере должны быть установлены [Docker](https://www.docker.com) и [docker-compose](https://docs.docker.com/compose/install/)
- Клонируйте репозиторий командой:
```
git clone https://github.com/mrvinil/foodgram-project-react.git
``` 
- Перейдите в каталог командой:
```
cd foodgram-project-react/backend/
``` 
- Выполните команду для запуска контейнера:
```
docker-compose up -d
``` 
- Выполните миграции:
```
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
``` 
- Команда для сбора статики:
```
docker-compose exec web python manage.py collectstatic --no-input
``` 
- Команда для создания суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

