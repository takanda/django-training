FROM python:latest

WORKDIR /app

COPY .devcontainer/api/requirements.txt .

RUN apt-get update \
    && apt-get install -y gcc sqlite3 \
    && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:10001" ]
