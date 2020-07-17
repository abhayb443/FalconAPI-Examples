import json, falcon
from waitress import serve


class ObjReq:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        validate_params = True

        if 'name' not in req.params:
            validate_params = False

        if 'age' not in req.params:
            validate_params = False

        if validate_params == True:
            output= {
                'name': req.params['name'],
                'age': req.params['age'],
            }
        else:
            output= {
                'error': "Required Parameter Name or Age is missing"
            }

        resp.body = json.dumps(output)


api = application = falcon.API()
api.add_route('/test', ObjReq())

serve(api, host='127.0.0.1', port=5555)
