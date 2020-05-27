from flask_restful import Resource, reqparse
from models.database import DatabaseInteract
from ast import literal_eval

class ReceiveData(Resource):

    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('data', action='append')

    def post(self):
        received_data = ReceiveData.parser.parse_args()
        insert_list=[]

        for items in received_data['data']:
            dict_items = literal_eval(items) # Desserializa o dicionário enviado pelo cliente
            
            try:
                insert_list.append(f'{dict_items["measurement"]},device_id={dict_items["device_id"]} {dict_items["data_type"]}={dict_items["value"]} {dict_items["timestamp"]}')
            except Exception as e:
                print(e)
                return {"message": "The server did not understand this request"},400
        data = DatabaseInteract(insert_list)

        result = data.insert() # Método que insere os dados do objeto no banco
        return result