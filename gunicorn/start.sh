#gunicorn starting

#!/bin/bash
source ../env/Scripts/activate
exec gunicorn --config gunicorn/gunicorn_config.py config.wsgi:application
