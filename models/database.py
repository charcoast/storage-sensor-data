from os import getenv
from influxdb_client import InfluxDBClient, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException

class DatabaseInteract():

  def __init__(self,data):
      self.data = data
      self.bucket = getenv('INFLUXDB_V2_BUCKET')
  def insert(self):
    client = InfluxDBClient.from_env_properties()
    write_api = client.write_api(write_options=SYNCHRONOUS)
    try:
      print(self.bucket)
      # write_precision padrão é nanosegundos, setado para segundo
      write_api.write(self.bucket,client.org,self.data,write_precision=WritePrecision.S)
    except ApiException as e:
        print(e)
        return {"message": "An error ocurred in the server-side"},500
    write_api.__del__()
    client.__del__()

    return {"message": "Created"},201
