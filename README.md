# Система обработки обращений клиентов

Учебный проект на Django + PostgreSQL для создания и хранения заявок клиентов.  
Проект запускается через Docker Compose.

## Технологии

- Python 3.12
- Django
- PostgreSQL 16
- Docker / Docker Compose

## Структура проекта

```text
backend/
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── sql/
│   └── seed_data.sql
└── my_project/
    ├── manage.py
    ├── my_project/
    ├── tickets/
    └── templates/
```

## Запуск

Перейти в папку `backend`:

```bash
cd backend
```

Запустить контейнеры:

```bash
docker-compose up --build
```

После запуска будут доступны:

```text
http://localhost:8000/
http://localhost:8000/tickets/create/
http://localhost:8000/admin/
```

## Миграции

В новом терминале выполнить:

```bash
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
```

## Создание администратора

```bash
docker-compose exec app python manage.py createsuperuser
```

## Заполнение базы тестовыми данными

Тестовые данные находятся в файле:

```text
sql/seed_data.sql
```

Для PowerShell:

```powershell
Get-Content .\sql\seed_data.sql -Encoding UTF8 | docker exec -i support_db psql -U postgres -d tickets
```

После этого в форме появятся клиенты, сотрудники, статусы, приоритеты, категории и каналы обращения.

## Остановка проекта

```bash
docker-compose down
```

Если нужно полностью удалить базу:

```bash
docker-compose down -v
```

## Проверка

Открыть форму:

```text
http://localhost:8000/tickets/create/
```

Заполнить заявку и отправить.  
Проверить сохранённые данные можно в админке:

```text
http://localhost:8000/admin/
```
