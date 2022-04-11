FROM python:3.10.2-alpine
WORKDIR /src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./
RUN pip install -r requirements.txt