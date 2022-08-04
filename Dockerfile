FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/movie

COPY ./requirements.txt/ usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/movie

EXPOSE 8000
CMD ["python", "namage.py", "runserver", "0.0.0.0:8000"]
