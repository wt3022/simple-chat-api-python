#!/usr/bin/env bash

script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
MYSQL_PWD=${DB_PASSWORD} mysql -u${DB_USERNAME} -h${DB_HOST} -e "drop database IF EXISTS ${DB_NAME};"
MYSQL_PWD=${DB_PASSWORD} mysql -u${DB_USERNAME} -h${DB_HOST} -e "create database IF NOT EXISTS ${DB_NAME};"
MYSQL_PWD=${DB_PASSWORD} mysql -u${DB_USERNAME} -h${DB_HOST} -e "drop database IF EXISTS test_${DB_NAME};"
MYSQL_PWD=${DB_PASSWORD} mysql -u${DB_USERNAME} -h${DB_HOST} -e "TRUNCATE mysql.general_log;"

