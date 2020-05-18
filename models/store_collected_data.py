from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS



#Suportar de inicio apenas temperatura
'''
Essa classe recebe:
device_id => Indica qual foi o dispositivo que enviou o dado, e consequentemente, de qual planta estamos falando. É a tag
measurement => Indica o tipo de medição (Ambiente ou planta). É o measurement
data_type => Indica o que está sendo medido (temperatura, umidade do solo, umidade do ar). É o field
value => É o valor que será gravado. É o set do field
'''
class CollectecDataModel():

    def __init__(self,device_id,measurement, data_type, value):
        self.device_id = device_id
        self.measurement = measurement
        self.data_type = data_type
        self.value = value
        self.token = "SECRET" 
        self.org = "SECRET" 
        self.bucket = "SECRET" 
  
    def insert(self):
        client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com",token=self.token) # Conceta
        write_api = client.write_api(write_options=SYNCHRONOUS) # Metodo write

        data = f"{self.measurement},device_id={self.device_id} {self.data_type}={self.value}" # os dados a serem inseridos
        write_api.write(self.bucket,self.org,data)# Insere o dado

        query = f'from(bucket: \"{self.bucket}\") |> range(start: -5s)' # Query de consulta
        tables = client.query_api().query(query, org=self.org) #Executa a query

        result = []
        for table in tables:
          for row in table.records:
            print(f'{row.values["_time"]}, {row.values["device_id"]}, {row.values["_field"]}, {row.values["_value"]}')
            result.append(str(row))
        return result
