# goit-sw-hw-06

Домашнє завдання: SQLAlchemy + PostgreSQL + Alembic

## Опис
У проєкті реалізовано:
- таблицю студентів
- таблицю груп
- таблицю викладачів
- таблицю предметів
- таблицю оцінок з датою отримання

## Технології
- Python
- SQLAlchemy
- PostgreSQL
- Alembic
- Faker
- Docker

## Запуск PostgreSQL
```bash
docker run --name my-postgres-db -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres