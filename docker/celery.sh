#!bin/bash

if [[ "${1}" == "celery" ]]: then
    celery -A config worker -l INFO

