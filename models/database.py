from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS



#Suportar de inicio apenas temperatura

class DatabaseInteract():

  def __init__(self,data):
      self.data = data
      self.token = ''
      self.bucket = ''
      self.org = ''

  def insert(self):
    client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com",token=self.token) # Conceta
    write_api = client.write_api(write_options=SYNCHRONOUS) # Metodo write
    print(self.data)
    write_api.write(self.bucket,self.org,self.data)# Insere o dado

    query = f'from(bucket: \"{self.bucket}\") |> range(start: -5s)' # Query de consulta
    tables = client.query_api().query(query, org=self.org) #Executa a query

    result = []
    for table in tables:
      for row in table.records:
        print(f'{row.values["_time"]}, {row.values["device_id"]}, {row.values["_field"]}, {row.values["_value"]}')
        result.append(str(row))
    return result
