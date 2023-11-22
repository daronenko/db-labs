#!/bin/sh

USER=root
PASSWORD=123
DB_NAME=$1

docker run \
    --name $DB_NAME -p 5432:5432 \
    -e POSTGRES_USER=$USER \
    -e POSTGRES_PASSWORD=$PASSWORD \
    -e POSTGRES_DB=$DB_NAME \
    -d postgres:16-alpine
