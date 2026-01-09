# Training Database API

Это REST API для управления информацией о тренировках и пользователях, реализованное с использованием FastAPI и SQLAlchemy с SQLite.

## Структура базы данных

### Пользователь (User)
- `id`: уникальный идентификатор пользователя (primary key)
- `user_id`: уникальный идентификатор пользователя (string, unique)
- `name`: имя пользователя (string)
- `training_type_1`: первый тип тренировки (string)
- `training_type_2`: второй тип тренировки (string)
- `training_type_3`: третий тип тренировки (string)
- `goal`: цель пользователя (string)
- `location`: место для тренировок (string)

### Тренировка (Training)
- `id`: уникальный идентификатор тренировки (primary key)
- `title`: название тренировки (string)
- `type`: тип тренировки (string)
- `monday`: описание понедельника (text, HTML разметка)
- `tuesday`: описание вторника (text, HTML разметка)
- `wednesday`: описание среды (text, HTML разметка)
- `thursday`: описание четверга (text, HTML разметка)
- `friday`: описание пятницы (text, HTML разметка)
- `saturday`: описание субботы (text, HTML разметка)
- `sunday`: описание воскресенья (text, HTML разметка)
- `user_id`: идентификатор пользователя (foreign key)

## API Endpoints

### Пользователи
- `POST /users/` - Создать нового пользователя
- `GET /users/` - Получить список пользователей
- `GET /users/{user_id}` - Получить пользователя по ID
- `PUT /users/{user_id}` - Обновить информацию о пользователе
- `DELETE /users/{user_id}` - Удалить пользователя

### Тренировки
- `POST /trainings/` - Создать новую тренировку
- `GET /trainings/` - Получить список тренировок
- `GET /trainings/{training_id}` - Получить тренировку по ID
- `PUT /trainings/{training_id}` - Обновить информацию о тренировке
- `DELETE /trainings/{training_id}` - Удалить тренировку

## Запуск локально

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите сервер:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

3. API будет доступен по адресу: http://localhost:8000

## Развертывание на Render.com

Файл `render.yaml` содержит конфигурацию для развертывания на Render.com.

## Требования

- Python 3.7+
- FastAPI
- SQLAlchemy
- Uvicorn