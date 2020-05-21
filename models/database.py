from influxdb_client import InfluxDBClient, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException

class DatabaseInteract():

  def __init__(self,data):
      self.data = data
      self.token = ''
      self.bucket = ''
      self.org = ''

  def insert(self):
    client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com",token=self.token) # Conceta
    write_api = client.write_api(write_options=SYNCHRONOUS) # Metodo write
    
    try:
      # write_precision padrão é nano segundos, setado para segundos
      write_api.write(self.bucket,self.org,self.data,write_precision=WritePrecision.S)
    except ApiException as e:
        print(e)
        return {"message": "An error ocurred in the server-side"},500
    write_api.__del__()
    client.__del__()
    
    return {"message": "Created"},201
