# Placify
[![Coverage Status](https://coveralls.io/repos/github/stirk1337/Placify/badge.svg?branch=main)](https://coveralls.io/github/stirk1337/Placify?branch=main)
![image](https://github.com/stirk1337/Placify/assets/63664630/616c72d9-b34c-4764-b0d6-aa62353d22e2)

## Цель
Создать веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещаемых местах.
# Описание задачи
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

## Что НЕ получилось
* Хотелось сделать, что после авторизация ссылка на аватарку сразу сохранялась, но как-то всё не получалось, и решил пока скачивать аватарку отдельно через VK API
* Немного кривой дизайн, но не фронт от слова совсем
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
