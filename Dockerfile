FROM python:3
COPY . /code
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV INFLUXDB_V2_URL 127.0.0.1
ENV INFLUXDB_V2_ORG org
ENV INFLUXDB_V2_TOKEN token
ENV INFLUXDB_V2_BUCKET bucket
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD flask run
