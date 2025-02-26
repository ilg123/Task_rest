# Task API

REST API для управления задачами, реализованное на FastAPI с использованием асинхронной SQLite и Docker.

##  Особенности

- Полный CRUD для задач
- Асинхронное взаимодействие с базой данных
- Автоматические миграции через Alembic
- Контейнеризация с Docker
- Временные метки в московском часовом поясе
- Валидация данных через Pydantic
- Инъекция зависимостей

## 🛠 Технологии

- Python 3.9
- FastAPI
- SQLite (асинхронный режим)
- Docker + Docker Compose
- Alembic (миграции)
- Pydantic
- SQLAlchemy

## 📋 Требования

- Docker 20.10+
- Docker Compose 2.0+

## ⚙️ Установка и запуск

1. Клонировать репозиторий:
```bash
git clone git@github.com:ilg123/Task_rest.git
```
2. Запустить сервис:
```bash
docker-compose up --build
```
3. Приложение будет доступно по адресу:
<http://localhost:8000/docs>

## 🚀 Особенности

- Полный CRUD для задач
- Асинхронное взаимодействие с базой данных
- Автоматические миграции через Alembic
- Контейнеризация с Docker
- Временные метки в московском часовом поясе
- Валидация данных через Pydantic
- Инъекция зависимостей

## 🛠 Технологии

- Python 3.9
- FastAPI
- SQLite (асинхронный режим)
- Docker + Docker Compose
- Alembic (миграции)
- Pydantic
- SQLAlchemy

## 📋 Требования

- Docker 20.10+
- Docker Compose 2.0+

## Пример тела запроса (POST/PUT)
```bash
{
  "title": "Название задачи",
  "description": "Описание задачи"
}
```

