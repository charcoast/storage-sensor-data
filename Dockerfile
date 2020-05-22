FROM python:3
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
CMD python app.py