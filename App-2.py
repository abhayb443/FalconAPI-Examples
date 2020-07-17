import falcon
import json
from waitress import serve


class ObjReq:
    def on_get(self, req, resp):

        resp.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        dic = {'Name': 'Abhay','Age': 26, 'Status': 'Employed', 'Type': 'IT'}

        doc = {
            'images': [
                dic
            ],

            'blows': [
                dic
            ]
        }

        output = {}

        if 'method' not in data:
            resp.status = falcon.HTTP_501
            output['name'] = 'Error, No method found in the request.'
        else:
            if data['method'] == 'on_get':
                output['name'] = doc.get('images')[0].get('Name')
            else:
                resp.status = falcon.HTTP_404
                output['name'] = None

        resp.body = json.dumps(output)


api = application = falcon.API()
api.add_route('/test', ObjReq())

serve(api, host='127.0.0.1', port=5555)
