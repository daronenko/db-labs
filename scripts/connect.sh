#!/bin/sh

USER=root
DB_NAME=$1

psql -h localhost -d $DB_NAME -U $USER -a
