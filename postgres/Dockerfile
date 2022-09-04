FROM postgres:14.5
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=qwerty123
ENV POSTGRES_DB=test_db
ADD CreateDB.sql /docker-entrypoint-initdb.d/
