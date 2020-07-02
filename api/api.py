from flask import Flask
from flask_restful import Resource, Api

import time

app = Flask(__name__)
api = Api(app)


class Video(Resource):
    def get(self):
        return {'time': time.time()}

api.add_resource(Video, '/video')

if __name__ == '__main__':
    app.run(debug=True)
