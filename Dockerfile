FROM python:3
COPY . /code
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD flask run
