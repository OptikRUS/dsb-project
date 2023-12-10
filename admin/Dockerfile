# установка python 3.11 с официального докерхаба
FROM python:3.11.6

# хост базы данных для докера
ENV DATABASE_HOST=database
# хост сайта
ENV SITE_HOST=0.0.0.0

# установка рабочей директории
WORKDIR /usr/src/admin

# Копирование файлов poetry
COPY pyproject.toml poetry.lock /usr/src/admin/

# установка зависимостей
RUN pip install poetry && poetry config virtualenvs.create false
RUN poetry install --no-ansi --no-cache

# копирование проекта
COPY . /usr/src/admin/