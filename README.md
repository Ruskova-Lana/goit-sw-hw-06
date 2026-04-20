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


## Run project
1. Start PostgreSQL:
docker run --name my-postgres-db -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

2. Install dependencies:
pip install -r requirements.txt

3. Run migrations:
alembic upgrade head

4. Seed database:
python seed.py

5. Run queries:
python main.py