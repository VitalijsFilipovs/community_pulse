# Community Pulse

**Community Pulse** — платформа для опросов, позволяющая анонимно выражать мнение по общественным вопросам.

## Основной стек:
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

## Основные эндпоинты
- **/questions** — работа с вопросами.
- **/categories** — работа с категориями.

## Запуск проекта
```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
uvicorn run:app --reload
