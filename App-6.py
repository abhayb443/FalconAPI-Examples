import falcon
from waitress import serve


class Authorise(object):
    def __init__(self, roles):
        self._roles = roles

    def __call__(self, req, resp, resource, params):
        if 'Admin' in self._roles:
            req.user_id = 1
        else:
            raise falcon.HTTPBadRequest("Bad Request", "You are not an admin right now,")


class ObjReq:

    @falcon.before(Authorise(['Admin', 'Normal', 'Guest']))
    def on_get(self, req, resp):
        print('trigger-get')
        output= {
            'method': 'get',
            'user-id': req.user_id
        }

        resp.media = output

    @falcon.before(Authorise(['Admin', 'Normal', 'Guest']))
    def on_post(self, req, resp):
        print('trigger-post')
        output = {
            'method': 'post',
            'user-id': req.user_id
        }

        resp.media = output


api = application = falcon.API()
api.add_route('/test', ObjReq())

serve(api, host='127.0.0.1', port=5555)
