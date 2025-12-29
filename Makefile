install:
	pip install uv
	pip install gunicorn uvicorn
	uv venv
	uv sync --frozen

dev:
	python manage.py runserver

lint:
	uv sync --dev
	uv run ruff check .

lint-fix:
	uv sync --dev
	uv run ruff check --fix .

start:
	python manage.py runserver

render-start:
	python manage.py migrate --noinput && gunicorn task_manager.wsgi

build:
	./build.sh

test:
	uv sync --dev
	uv run python manage.py test

test-cov:
	uv sync --dev
	uv run coverage run ./manage.py test
	uv run coverage xml

migrate:
	python manage.py migrate

sync:
	uv sync

migrations:
	python manage.py makemigrations

migrations-user:
	python manage.py makemigrations user

collectstatic:
	python manage.py collectstatic --no-input

translate-compile:
	django-admin compilemessages

translate-makemessages:
	django-admin makemessages -l ru
