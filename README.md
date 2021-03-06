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



## Usando a API
* POST /send <br/> 
aceita o seguinte formato:
```
{
  "data":[
    {"device_id":"device-1","measurement":"room","data_type":"temperature","value":25.0, "timestamp":1589984618},
    {"device_id":"device-2","measurement":"kitchen","data_type":"temperature","value":24.5, "timestamp":""},
    {"device_id":"device-3","measurement":"bedroom","data_type":"temperature","value":24.3, "timestamp":""},
    {"device_id":"device-4","measurement":"closet","data_type":"temperature","value":26, "timestamp":""},
    {"device_id":"device-5","measurement":"garden","data_type":"temperature","value":22, "timestamp":""}
    ]
}
```

* GET /ping<br/>
Retorna 200OK quando o servidor está up.
