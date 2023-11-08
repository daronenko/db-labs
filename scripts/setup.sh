#!/bin/sh

USER=root
PASSWORD=1234
DB_NAME=$1

docker run \
    --name postgres-stand -p 5432:5432 \
    -e POSTGRES_USER=$USER \
    -e POSTGRES_PASSWORD=$PASSWORD \
    -e POSTGRES_DB="$DB_NAME" \
    -d postgres:16-alpine \
&& sleep 3 \
&& psql -h localhost -d "$DB_NAME" -U $USER -a
