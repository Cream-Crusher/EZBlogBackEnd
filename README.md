# EZBlogBackEnd

Проект сайта блогов с использованием микросервисов и чистой архитектуры

## Микросервисы

* database_service: Представление логики базы данных
* auth_service: Предсталвение логики login/logout

### Особенности

* Каждый микросервис является самостоятельным за счет использования микросервисной архитектуры

## Глобальный стек

* Python
* FastAPI
* SQLAlchemy
* alembic
* asyncio
* aiohttp
* unittest
* environs

## Базы данных

* PostgreSQL + asyncpg
* Redis
* MongoDB

## Инструменты

* Docker
* CI CD
* swagger
