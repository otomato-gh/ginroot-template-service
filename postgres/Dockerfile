FROM postgres:14.5
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=qwerty123
ENV POSTGRES_DB=test_db
ADD 01_CreateDB.sql /docker-entrypoint-initdb.d/
ADD 02_TestEntries.sql /docker-entrypoint-initdb.d/
