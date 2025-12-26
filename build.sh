# Устанавливаем uv
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Устанавливаем зависимости
uv sync --frozen

# Миграции и статика
uv run python manage.py collectstatic --noinput
uv run python manage.py migrate

echo "✅ Build completed!"
