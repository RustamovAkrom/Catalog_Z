#gunicorn configurations

bind = "127.0.0.1:8000"
workers = 3
timeout = 120
accesslog = 'gunicorn/logs/access.log'
errorlog = 'gunicorn/logs/error.log'
loglevel = 'info'
