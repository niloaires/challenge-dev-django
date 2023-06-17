FROM python:3.8

RUN apt-get update && apt-get install -y \
    wget \
    sudo  \
    curl  \
    gnupg2 -y \
    nano \
    && rm -rf /var/lib/apt/lists/* \
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000

