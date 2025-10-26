# Smart Library System

## Описание

**Smart Library System** — демонстрационная система управления библиотекой с **многоуровневой архитектурой**:

- **Контроллеры** — обработка HTTP-запросов и взаимодействие с клиентом
- **Сервисы** — бизнес-логика [регистрация пользователей, добавление и выдача книг]
- **Репозитории** — работа с данными в памяти

**Функционал:**

- Регистрация пользователей
- Добавление книг
- Выдача книг пользователям
- Просмотр списка всех пользователей и всех книг

[GitHub репозиторий проекта](https://github.com/Sensi57/SA_Assignment)

---

## ⚙️ Требования

- Python 3.10+
- FastAPI
- Uvicorn

---

## Установка и запуск

### Клонирование репозитория

```bash
git clone https://github.com/Sensi57/SA_Assignment.git
cd SA_Assignment/server
```

### Создание и активация виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate
```

### Установка зависимостей

```bash
pip3 install -r requirements.txt
```

### Запуск приложения

```bash
uvicorn main:app --reload
```

## Пример использования

### Регистрация пользователя

```bash
POST /users/register
Body:
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Выдача книги

```bash

POST /books/borrow
Body:
{
  "user_id": 1,
  "book_id": 2
}
```
