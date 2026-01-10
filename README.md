# Диспетчер задач

## Hexlet tests and linter status:
[![Actions Status](https://github.com/HidTired/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/HidTired/python-project-52/actions)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=HidTired_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=HidTired_python-project-52)

## Описание
Диспечер задач на основе Django,позволяет создавать, управлять задачами с помощью статусов и меток.

## Клонировать репозиторий
 - git clone https://github.com/HidTired/python-project-52.git

## Перейти в проект
 - cd python-project-52

## Создать виртуальное окружение
 - python -m venv .venv

## Активировать виртуальное окружение
 - .venv\Scripts\Activate.ps1

## Установить зависимости
 - pip install -e .
 - python manage.py migrate

## Запуск
 - python manage.py runserver

Адрес : http://localhost:8000

## Возможности:

 - Регистрация и авторизация
 - Управление задачами
 - Статусы и метки, использующиеся для задач