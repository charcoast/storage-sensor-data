from flask_restful import Resource, reqparse
from models.store_collected_data import CollectecDataModel

class ReceiveData(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)

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

    def post(self):
        received_data = ReceiveData.parser.parse_args()
        data = CollectecDataModel(received_data['device_id'],received_data['measurement'],received_data['data_type'],received_data['value'])

        result = data.insert()
        return result
        