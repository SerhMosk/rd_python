FROM python:latest

ENV APP_HOME=/app

WORKDIR $APP_HOME

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

#CMD python manage.py runserver 0.0.0.0:8080
