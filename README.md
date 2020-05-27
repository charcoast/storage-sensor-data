# Storage-sensor-data
Esta API tem o objetivo de gravar os dados de ambiente coletados por Arduinos em um banco de dados InfluxDB. 

Será utilizado no contexto do Projeto Integrador da 8ª Fase do Curso Técnico Integrado de Telecomunicações.


## Como iniciar o projeto
1. Clonar o repositório

```git clone https://github.com/charcoast/storage-sensor-data```

2. Acessar a pasta e executar o docker build

```docker build -t flaskapp .```

3. Iniciar o container

```docker container run -d -p 5000:5000 flaskapp```
