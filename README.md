# Catalog_Z
![img](https://github.com/RustamovAkrom/Catalog_Z/blob/main/logo.jpg?raw=true)

## Created in Django 

## Run Worker Celery
### - Ubuntu or Linux
+ pleace install redis in Ubuntu on Linux
    ~~~ 
    sudo service redis-server start
    ~~~

    ~~~
    celery -A config worker -l INFO
    ~~~

 ## Run project: 
 - CMD
    ~~~
    python -m venv env
    ~~~

    ~~~
    - windows: env\Scripts\activate | - linux: source env/bin/activate
    ~~~

    ~~~
    pip install -r requirements.txt
    ~~~

    ~~~
    python manage.py runserver
    ~~~

---
# Menu:
 + ### [Photos](http://127.0.0.1:8000/photos/) 📷 
 + ### [Videos](http://127.0.0.1:8000/videos/) 📽️
 + ### [About](http://127.0.0.1:8000/photos/about/) 🧾
 + ### [Contact](http://127.0.0.1:8000/photos/contact/) 📞

 
