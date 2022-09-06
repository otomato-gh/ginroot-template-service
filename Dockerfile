FROM python:3.10-slim-buster
ENV SERVER_PORT 80
EXPOSE 80
WORKDIR /template-service
COPY pyproject.toml poetry.lock ./
COPY /app ./app
RUN pip install poetry && poetry install
ENTRYPOINT ["poetry", "run", "start"]
