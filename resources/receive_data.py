from flask_restful import Resource, reqparse
from models.database import DatabaseInteract
from marshmallow import Schema, fields, pprint
import json
from ast import literal_eval

class ReceiveData(Resource):

    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('data', action='append')

    def post(self):
        received_data = ReceiveData.parser.parse_args()
        insert_list=[]
        for items in received_data['data']:
            dict_items = literal_eval(items)
            insert_list.append(f'{dict_items["measurement"]},device_id={dict_items["device_id"]} {dict_items["data_type"]}={dict_items["value"]}')
        
        data = DatabaseInteract(insert_list)

        result = data.insert()
        return result


'''
    parser.add_argument('device_id',
    type=str, required=True,
    help="device_id Can't be left blank")
    
    parser.add_argument('measurement',
    type=str, required=True,
    help="measurement Can't be left blank")

    parser.add_argument('data_type',
    type=str, required=True,
    help="data_type Can't be left blank")

    parser.add_argument('value',
    required=True,
    help="value Can't be left blank")
    '''