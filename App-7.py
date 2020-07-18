import falcon
from waitress import serve
import base64

user_account = {
    'Abhay': 'Abhay'
}

class Authorise(object):
    def __init__(self):
        pass

    def _auth_basic(self, username, password):
        if username in user_account and user_account[username] == password:
            print("You have the required access, Welcome")
        else:
            raise falcon.HTTPUnauthorized('Unauthorised', 'You do not have the required access, Sorry')

    def __call__(self, req, resp, resource, params):
        print("Before Trigger - Class Authorise")
        auth_exp = req.auth.split(" ") if req.auth is not None else (None, None, )

        if auth_exp[0] is not None and auth_exp[0].lower() == 'basic':
            auth = base64.b64decode(auth_exp[1]).decode('utf-8').split(':')
            username = auth[0]
            password = auth[1]
            self._auth_basic(username, password)
        else:
            raise falcon.HTTPNotImplemented("Not Implemented", "You don't have the right auth method")


class ObjReq:
    @falcon.before(Authorise())
    def on_get(self, req, resp):
        print('trigger-get')
        output= {
            'method': 'get',
        }

        resp.media = output


api = application = falcon.API()
api.add_route('/test', ObjReq())

serve(api, host='127.0.0.1', port=5555)
