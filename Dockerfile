# pull official base image
FROM python:3.11.3-alpine

# set work directory
WORKDIR /usr/src/app

# install psycopg2
RUN apk update \
    && apk add --virtual build-dependencies build-base gcc python3-dev musl-dev libffi-dev openssl-dev

RUN apk add --update tzdata
ENV TZ=Africa/Cairo

# work dir
WORKDIR /usr/src/app

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

RUN  mkdir -p /usr/src/app/static/
RUN chmod 755 /usr/src/app/static/


COPY . .
COPY requirements.txt .
RUN pip3 install gunicorn
RUN pipenv requirements > requirements.txt
RUN pip3 install -r requirements.txt

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 80

CMD ["gunicorn", "--chdir", "/usr/src/app", "--bind", "8080:80", "newspluse.wsgi:application"]
