# Storage-sensor-data
Esta API tem o objetivo de gravar os dados de ambiente coletados por Arduinos em um banco de dados InfluxDB. 

Será utilizado no contexto do Projeto Integrador da 8ª Fase do Curso Técnico Integrado de Telecomunicações.


## Como iniciar o projeto
1. Clonar o repositório

```git clone https://github.com/charcoast/storage-sensor-data```

2. Acessar a pasta e editara as variáveis de ambiente no Dockerfile referentes ao InfluxDB
```
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
```
3. Executar o docker build

```docker build -t flaskapp .```

4. Iniciar o container

```docker container run -d -p 5000:5000 flaskapp```
