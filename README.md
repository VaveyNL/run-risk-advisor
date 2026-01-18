# Run Risk Advisor

Run Risk Advisor - учебный веб-сервис для планирования пробежек и оценки риска тренировки на основе погодных условий и качества воздуха (PM2.5).

Сервис позволяет пользователю создавать планы пробежек, автоматически получать рекомендации и анализировать историю рисков.

Ссылка на развернутый проект  
- https://run-risk-advisor-atb8.onrender.com

## Основной функционал
- настройка профиля пользователя (город, чувствительность, лимит PM2.5)
- создание плана пробежки (дата, время, длительность, интенсивность)
- автоматическое получение данных погоды и воздуха через OpenWeather API
- расчет итогового риска пробежки (0–100)
- формирование текстовой рекомендации
- хранение истории рекомендаций
- визуализация данных в виде графика
- поддержка тёмной и светлой темы
- поддержка RU / EN интерфейса

## Используемые технологии
- Python
- Django
- SQLite
- Requests
- Pandas
- Plotly
- Bootstrap
- Gunicorn

## Запуск проекта локально

Создайте и активируйте виртуальное окружение:
```
python -m venv venv
venv\Scripts\activate
```

Установите зависимости:
```
pip install -r requirements.txt
```

Создайте файл .env в корне проекта:
```

DJANGO_SECRET_KEY=django-insecure-change-me
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_KEY
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Выполните миграции:
```
python manage.py migrate
```

Создайте администратора:
```
python manage.py createsuperuser
```

Запустите сервер:
```
Запустите сервер:
python manage.py runserver

```

Откройте сайт:
```
http://127.0.0.1:8000
```

Админ-панель:
```
http://127.0.0.1:8000/admin/
```

Deploy:
```
Проект развёрнут на платформе Render.com

Используемые команды сборки:

collectstatic

migrate

```

Команда запуска сайта:
```
gunicorn config.wsgi:application
```