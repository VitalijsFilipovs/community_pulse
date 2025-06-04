# Community Pulse

**Community Pulse** — это интерактивная платформа, которая позволяет анонимно создавать вопросы на общественно значимые темы и получать мнения других участников. Она помогает измерять общественное настроение и демонстрирует, как теоретические знания Flask, SQLAlchemy и Pydantic применяются на практике.

## 🚀 Основные функции

- **Создание вопросов:**
  Пользователи могут создавать новые вопросы, чтобы другие могли ответить "согласен" или "не согласен".

- **Ответы на вопросы:**
  Пользователи видят список вопросов и могут выбрать свою позицию (согласен/не согласен).

- **Статистика ответов:**
  Для каждого вопроса доступна статистика количества согласных и несогласных пользователей.

## ⚙️ Технологический стек

- **Flask** — микрофреймворк для построения API.
- **Flask-SQLAlchemy** — для работы с базой данных.
- **Alembic** — управление миграциями.
- **Pydantic** — сериализация и валидация данных.

## 📁 Структура проекта

/community_pulse/
├── app/
│ ├── init.py
│ ├── models/
│ │ ├── init.py
│ │ ├── category.py
│ │ ├── questions.py
│ │ └── response.py
│ ├── routers/
│ │ ├── init.py
│ │ ├── categories.py
│ │ ├── questions.py
│ │ └── response.py
│ └── schemas/
│ ├── init.py
│ ├── category.py
│ ├── question.py
│ └── response.py
├── instance/
│ └── community_pulse.db
├── migrations/
├── config.py
├── main.py
├── run.py
├── requirements.txt
└── README.md

## 📝 Установка и запуск

1. **Клонируй репозиторий:**
    ```bash
    git clone https://github.com/username/community_pulse.git
    cd community_pulse
    ```

2. **Создай и активируй виртуальное окружение:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate     # Для Windows
    ```

3. **Установи зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Применяй миграции:**
    ```bash
    flask db upgrade
    ```

5. **Запусти сервер:**
    ```bash
    flask run
    ```

Приложение будет доступно по адресу: http://127.0.0.1:5000.
