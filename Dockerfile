# pull official base image
FROM python:3.11.3-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies for psycopg2 and Django
RUN apk update && apk add --no-cache \
    build-base \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
    openssl-dev \
    tzdata \
    postgresql-dev

# set timezone
ENV TZ=Africa/Cairo

# upgrade pip & install pipenv
RUN pip3 install --upgrade pip
RUN pip3 install pipenv gunicorn

# copy files
COPY requirements.txt ./
RUN pipenv requirements > requirements.txt || true
RUN pip3 install -r requirements.txt

COPY . .

# create static dir
RUN mkdir -p /usr/src/app/static/ && chmod 755 /usr/src/app/static/

# run Django migrations & collectstatic
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# expose port
EXPOSE 80

# start server with gunicorn
CMD ["gunicorn", "--chdir", "/usr/src/app", "--bind", "0.0.0.0:80", "newspluse.wsgi:application"]
