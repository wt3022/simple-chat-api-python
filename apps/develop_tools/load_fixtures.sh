#!/bin/bash

script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)

cd $script_dir/..

python manage.py migrate
python manage.py loaddata fixtures/develop.json
