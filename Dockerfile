FROM python:3.11.9

RUN mkdir /Catalog_Z

WORKDIR /Catalog_Z

COPY requirements.txt .

RUN  pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]