# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY modules.spec requirements.req
RUN pip install -r requirements.req
EXPOSE 5000
COPY . .
CMD ["flask", "run"]

