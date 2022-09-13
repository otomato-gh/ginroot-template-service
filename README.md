# ginroot-template-service
The template microservice

## Set up the development environment
 
Follow [instructions](CONTRIBUTING.md).

## Build and launch Postgres in Docker to work with the service
```bash
cd postgres
docker build . -t my-postgres
docker run -d -p 5432:5432 my-postgres
```

## Launch application
Export [environment variables](example_env/.env_app).
Then run:
```bash
uvicorn app.main:app --reload --port 8000
```

## Test application
Export [environment variables](example_env/.env_app).
Then run from the [app](./app) directory:
```bash
pytest
```
