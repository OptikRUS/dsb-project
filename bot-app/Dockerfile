# установка python 3.11 с официального докерхаба
FROM python:3.11.6
# хост базы данных для докера
#ENV DATABASE_HOST=database
# установка рабочей директории
WORKDIR /usr/src/bot-app

# Копирование файлов poetry
COPY pyproject.toml poetry.lock /usr/src/bot-app/

# установка зависимостей
RUN pip install poetry && poetry config virtualenvs.create false
RUN poetry install --no-ansi --no-cache

# копирование проекта
COPY . /usr/src/bot-app/