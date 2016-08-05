FROM python:3.5-alpine

WORKDIR /build
ENV CONFIG_CLASS=Production

RUN apk add --no-cache git postgresql-dev gcc python3-dev musl-dev libffi-dev

# Install dependencies so we can cache this build step after code changes still
ADD ["models", "./models"]
ADD ["requirements.txt", "./"]

RUN pip install -r requirements.txt && pip install gunicorn

# Actually add everything now
COPY ["./", "./"]

CMD gunicorn -b 0.0.0.0:80  --timeout=240 --workers=4 wsgi:app