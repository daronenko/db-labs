#!/bin/sh

set USER dan
set PASSWORD 1234
set DB "$1"

docker run \
    -d --name postgres \
    -p 5432:5432 \
    -e POSTGRES_USER="$USER" \
    -e POSTGRES_PASSWORD="$PASSWORD" \
    -e POSTGRES_DB="$DB" \
    postgres:16-alpine \
&& sleep 3
