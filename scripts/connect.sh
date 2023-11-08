#!/bin/sh

USER=root
PASSWORD=1234
DB_NAME=$1

psql -h localhost -d "$DB_NAME" -U $USER -a
