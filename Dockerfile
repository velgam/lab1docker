# ============================================
# Стадия 1: builder — установка зависимостей
# ============================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Копируем ТОЛЬКО файл зависимостей — для кэширования слоёв
COPY requirements.txt .

# Устанавливаем зависимости в /root/.local
RUN pip install --no-cache-dir --user -r requirements.txt

# ============================================
# Стадия 2: финальный образ — только runtime
# ============================================
FROM python:3.11-slim

WORKDIR /app

# Копируем установленные зависимости из builder-стадии
COPY --from=builder /root/.local /root/.local

# Копируем код приложения
COPY ./app ./app

# Делаем утилиты из /root/.local доступными в PATH
ENV PATH=/root/.local/bin:$PATH

# Документируем порт (gunicorn будет слушать 8000)
EXPOSE 8000

# Запуск через gunicorn (production WSGI-сервер)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app()"]