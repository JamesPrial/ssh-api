import subprocess

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Authorized_keys(Resource):
    
    def get(self, user):
        try:
            with open(f"/home/{str(user)}/.ssh/authorized_keys", 'r') as authkeys_file:
                keys = []
                for line in authkeys_file:
                    keys.append(line.strip())
                return jsonify({'authorized_keys': keys})
        except FileNotFoundError:
            return '', 404
        except PermissionError:
            return '', 403
        
    def put(self, user):
        try:
            data = request.get_json()
            key = data['key']
            with open(f"/home/{str(user)}/.ssh/authorized_keys", 'a') as authkeys_file:
                authkeys_file.write("\n%s\n" % key)
                return '', 204
        except KeyError:
            return '', 400
        except FileNotFoundError:
            return '', 404
        except PermissionError:
            return '', 403
        
    def delete(self, user):
        try:
            data = request.get_json()
            key = data['key']
            keys_to_keep = []
            with open(f"/home/{str(user)}/.ssh/authorized_keys", 'r') as authkeys_file:
                for line in authkeys_file:
                    if line.strip() != key.strip():
                        keys_to_keep.append(line)
            with open(f"/home/{str(user)}/.ssh/authorized_keys", 'w') as authkeys_file:
                authkeys_file.writelines(keys_to_keep)
            return '', 204
        except KeyError:
            return '', 400
        except FileNotFoundError:
            return '', 404
        except PermissionError:
            return '', 403



api.add_resource(Authorized_keys, '/<string:user>')
if __name__ == '__main__':
    run()
