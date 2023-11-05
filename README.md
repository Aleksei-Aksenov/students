# api_yamdb

![badge](https://user-images.githubusercontent.com/86766017/175809946-525c22c7-c999-4101-85e0-f284ee3ac198.svg)

## Проект Students

Позволяет добавлять студентов в список, редактировать и удалять данные о студентах.

### Над проектом работали:

- Алексей Аксенов
  https://github.com/Aleksei-Aksenov

### Стек технологий:

![python](https://user-images.githubusercontent.com/86766017/175810761-2a172f41-70a4-47d9-9c70-e645f018a5e4.svg)
![drf](https://user-images.githubusercontent.com/86766017/175810765-3c6dc2fd-9484-4487-beff-202db318fd56.svg)

## Как установить и запустить проект

# Запуск бэкенда:

- git clone
- cd finalstud
- cd backend
- python -m venv venv
- source venv/Scripts/activate
- python -m pip install --upgrade pip
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

## Примеры запросов

Получение списка всех студентов

**GET /api/students/**

Получить список всех отзывов к определенному произведению по его id

# Запуск фронтенда:

Перейдите на официальный сайт https://nodejs.org/en/download и скачайте последнюю стабильную версию с припиской LTS (Node.js помогает JavaScript взаимодействовать с устройствами ввода-вывода через свой API и подключать разные внешние библиотеки).
Через терминал Установите Vue CLI:

- npm install -g @vue/cli
  Перейдите в папку frontend проекта finalstud и запустите проект на локальном сервере:
- cd finalstud
- cd frontend
- npm run serve
  Протестируйте работу фронтенда проекта открыв его в браузере по адресу http://localhost:8080/
