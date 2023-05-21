# Placify http://stirk2023.pythonanywhere.com/
![logo](https://github.com/stirk1337/Placify/assets/63664630/9abc4293-f068-44b7-a685-29e3472c707d)
[![Coverage Status](https://coveralls.io/repos/github/stirk1337/Placify/badge.svg?branch=main)](https://coveralls.io/github/stirk1337/Placify?branch=main)

## Цель
Создать веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещаемых местах.
## Описание задачи
Пользователь заходит на сайт и видит страницу с кратким описанием сервиса. Также, он замечает кнопки “Войти с помощью Google” (или VK, на Ваше усмотрение), нажимая на которую Google/VK предлагает ему разрешить доступ к его базовой информации.

## Что получилось
* Смог реализовать весь нужный функционал. 
  + Авторизация VK
  + Добавление новых мест
  + Отображение мест на главной
  + Выход из аккаунта
* Авторизация VK через приложение social-django и получение данных через VK API
* Отображение карт через Yandex Maps API
* Стили bootstrap 
* Coveralls.io бейдж с процентами покрытия тестами
  + Почему-то он показывает 76%, хотя coverage показывал мне 99% на локальной машине. Скорее всего это из-за того, что в тестах методы не запускаются напрямую, а через фейковые запросы

## Что НЕ получилось
* Хотелось сделать, что после авторизация ссылка на аватарку сразу сохранялась, но как-то всё не получалось, и решил пока скачивать аватарку отдельно через VK API
* Немного кривой дизайн, но я не фронт от слова совсем
* Хотел прикрутить тесты на .pre-commit-config.yml, но вышла странная ситуация: Я сейчас на Windows и чтобы запустить интерпретатор мне нужно написать "py". На Linux же другая команда, соотвественно .pre-commit-config не давал мне запушить. Хотел бы как-то решить этот конфликт с разными системами, не прибегая к тому чтобы писать только на Linux. 

## Запуск
```
docker-compose up
```
## Домен
Приложение будет доступно на:
```
127.0.0.1:8000
```
## Тесты 
```
python3 placify/manage.py test
```
