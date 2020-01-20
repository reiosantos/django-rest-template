FROM python:3.7

RUN apt-get update && \
apt-get install -y --fix-missing python3-dev libjpeg-dev nginx supervisor pdftk && \
echo "daemon off;" >> /etc/nginx/nginx.conf && \
mkdir /var/log/django_rest_template/ && \
rm -rf /var/lib/apt/lists/*

ENV DJANGO_SETTINGS_MODULE=django_rest_template.settings.docker ENV=local \
DB_HOST=db DB_NAME=django_rest_template DB_USERNAME=django_rest_template DB_PASSWORD=django_rest_template DB_PORT=3306 \
EMAIL_HOST_PASSWORD=********

WORKDIR /usr/src/app/
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /usr/src/app/

RUN bash -c "python manage.py check"

RUN bash -c "python manage.py collectstatic --noinput"

RUN bash -c "chmod +x ./docker/run.sh"

EXPOSE 8000 90

CMD ["./docker/run.sh"]
