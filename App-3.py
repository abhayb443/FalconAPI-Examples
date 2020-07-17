import json, falcon
from waitress import serve


class ObjReq:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        output = {
            "MSG": 'Hello {}'.format(data['name'])
        }

        resp.body = json.dumps(output)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        data = json.loads(req.stream.read())

        concater = str(data['First']) + '.' + str(data['Last'])

        output = {
            "MSG": "Hello {} {} adder gives {}".format(data['First'], data['Last'], concater)
        }
        resp.body = json.dumps(output)


api = application = falcon.API()
api.add_route('/test', ObjReq())

serve(api, host='127.0.0.1', port=5555)
