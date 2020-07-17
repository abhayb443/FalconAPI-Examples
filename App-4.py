import json, falcon
from waitress import serve


class ObjReq:

    __json_content = {}

    def __validate_json_input(self, req):
        try:
            self.__json_content = json.loads(req.stream.read())
            return True

        except ValueError as e:
            self.__json_content = {}
            return False

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        validated = self.__validate_json_input(req)

        output = {
            "status": 200,
            "name": None
        }

        if validated == True:
            if 'name' in self.__json_content:
                output["name"] = 'Hello {}'.format(self.__json_content['name'])
            else:
                output["status"] = 404
                output["name"] = "Json Input needs name keyword"
        else:
            output["status"] = 404
            output["name"] = "Json Input is not validated"

        resp.body = json.dumps(output)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        data = json.loads(req.stream.read())

        concater = str(data['First']) + '.' + str(data['Last'])

        output = {
            "name": "Hello {} {} adder gives {}".format(data['First'], data['Last'], concater)
        }
        resp.body = json.dumps(output)


api = application = falcon.API()
api.add_route('/test', ObjReq())

serve(api, host='127.0.0.1', port=5555)
