# from flask import Flask, jsonify, request

# app = Flask(__name__)

# languages = [{'name': 'Javascript'}, {'name': 'Python'}]


# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({'message': 'it works'})


# @app.route('/postman', methods=['POST'])
# def return_post():
#     # language = {'name': request.json['name']}
#     # languages.append(language)
#     some_var = request.get_json()
#     return jsonify(languages)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='3000', debug=True)

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

power_json = {'on': False}


class LEDPower(Resource):
    def get(self):
        return {'on': 'true'}

    def post(self):
        power_json = request.get_json()
        if power_json['on'] == True:
            power_json['on'] = False
            print('it is on, turn it off')

            # Turn led off or on here
            return {'Success': power_json}, 201
        else:
            power_json['on'] = True
            print('it is off, turn it on')

            # Turn led off or on here
            return {'Success': power_json}, 201


class Multi(Resource):
    def get(self, num):
        return {'result': num * 10}


api.add_resource(LEDPower, '/api/ledpower')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)
