
## Проект Students

Позволяет добавлять студентов в список, редактировать и удалять данные о студентах.

### Над проектом работал:

- Алексей Аксенов
  https://github.com/Aleksei-Aksenov

### Стек технологий:

![python](https://user-images.githubusercontent.com/86766017/175810761-2a172f41-70a4-47d9-9c70-e645f018a5e4.svg)
![drf](https://user-images.githubusercontent.com/86766017/175810765-3c6dc2fd-9484-4487-beff-202db318fd56.svg)
![vue](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D.svg)

## Как установить и запустить проект

# Запуск бэкенда:

- Склонируйте репозиторий: git clone https://github.com/Aleksei-Aksenov/students
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

**GET http://127.0.0.1:8000/api/students/**
![image](https://github.com/Aleksei-Aksenov/students/assets/99750013/b802dc3d-f2cf-42eb-9b53-baa9a414a9fc)

____
Добавить нового студента
{
    "name": "Джек Дэниелз",
    "group": "УРА-001"
}

**POST http://127.0.0.1:8000/api/students/**
![image](https://github.com/Aleksei-Aksenov/students/assets/99750013/680169f6-664f-4c6f-b4f0-6e95bc60599b)
____
Редактировать студента c id=15
{
    "name": "Джекки Дэниелзович",
    "group": "УРА-001"
}

**PUT http://127.0.0.1:8000/api/students/15/**
![image](https://github.com/Aleksei-Aksenov/students/assets/99750013/1e261752-0716-4069-a70c-4f9e39151f03)
____
Удалить студента c id=15

**DELETE http://127.0.0.1:8000/api/students/15/**
![image](https://github.com/Aleksei-Aksenov/students/assets/99750013/f74214e6-70db-4fda-84ac-85cbc8566729)

# Запуск фронтенда:

- Перейдите на официальный сайт https://nodejs.org/en/download и скачайте последнюю стабильную версию Node.js
- Через терминал установите Vue CLI:  npm install -g @vue/cli
- Перейдите в папку frontend проекта finalstud и запустите проект на локальном сервере:
- cd finalstud
- cd frontend
- npm run serve
  Протестируйте работу фронтенда проекта открыв его в браузере по адресу http://localhost:8080/

  
![image](https://github.com/Aleksei-Aksenov/students/assets/99750013/a1004c40-96cc-4a77-82f2-4ffd01f1f5b6)
