FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-basic
WORKDIR /django-basic
ADD requirements.txt /django-basic/
RUN pip install pip 
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /django-basic/
