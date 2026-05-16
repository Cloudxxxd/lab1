# lab1

## Описание

Простое веб-приложение на Python с использованием FastAPI.

Приложение обрабатывает GET-запрос по маршруту:

```bash
/info
```

и возвращает JSON с количеством дней до Нового года.

---

## Запуск без Docker

Установка зависимостей:

```bash
py -m pip install fastapi uvicorn
```

Запуск приложения:

```bash
py -m uvicorn main:app --reload
```

После запуска открыть:

```bash
http://127.0.0.1:8000/info
```

---

## Запуск через Docker

Сборка и запуск контейнера:

```bash
docker-compose up --build
```

После запуска открыть:

```bash
http://localhost:8000/info
```

---

## Пример ответа

```json
{
    "days_before_new_year": 229
}
```
