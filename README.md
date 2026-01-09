# Клонировать репозиторий
git clone https://github.com/HidTired/python-project-52.git
cd python-project-52

# Создать виртуальное окружение
python -m venv .venv

# Активировать виртуальное окружение
.venv\Scripts\Activate.ps1

# Установить зависимости
pip install -e .
python manage.py migrate

# Запуск
python manage.py runserver

Адрес : http://localhost:8000

# Возможности:

 - Регистрация и авторизация
 - Управление задачами
 - Статусы и метки, использующиеся для задач