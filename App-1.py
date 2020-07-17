import falcon
import json
from waitress import serve


class ObjReq:
    def on_get(self, req, resp):
        dic = {'Name': 'Abhay', 'Age': 26, 'Status': 'Employed', 'Type': 'IT'}

        doc = {
            'images': [
                dic
            ],

            'blows': [
                dic
            ]
        }

        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    # def on_post(self, req, resp):

api = application = falcon.API()
api.add_route('/test', ObjReq())

serve(api, host='127.0.0.1', port=5555)
