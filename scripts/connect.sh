#!/bin/sh

set USER dan
set DB "$1"

psql -h localhost -d "$DB" -U "$USER"
