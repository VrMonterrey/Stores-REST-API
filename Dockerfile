FROM python3.11
EXPOSE 5000
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
COPY . /app/
ENV FLASK_ENV=production
CMD ["flask", "run", "--host=0.0.0.0"]