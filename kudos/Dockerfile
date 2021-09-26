
FROM python:3
ENV LANG C.UTF-8


RUN mkdir /django

#RUN apt-get -y update
#RUN apt-get install -y python python-pip python-dev python-psycopg2 postgresql-client 

ADD requirements.txt /django/requirements.txt
RUN pip3 install -r /django/requirements.txt

#RUN apt-get -y update && apt-get -y autoremove
WORKDIR /django
COPY . ./
EXPOSE 8000

RUN python manage.py makemigrations
#RUN python manage.py migrate

CMD ["python" ,"manage.py", "runserver", "0.0.0.0:8000" ]