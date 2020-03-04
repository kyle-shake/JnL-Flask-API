#backend/server/app.py

import os


from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from server.database.db import initialize_db
from flask_cors import CORS, cross_origin
from flask_restful import Api
from server.resources.routes import init_routes

#Init app
app = Flask(__name__)
app_settings = os.getenv(
    'APP_SETTINGS',
    'server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)


#Init Database
app = initialize_db(app)

#cPanel Hosting requires 'application' variable in passenger_wsgi
application = app

#Init API
api = Api(app)
#Handle CORS
CORS(app, resources=r'/api/*')



#Encryption
bcrypt = Bcrypt(app)

#Init JSON Web Token Manager
jwt = JWTManager(app)

# from backend.server.auth.views import auth_blueprint
# app.register_blueprint(auth_blueprint)

init_routes(api)

if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)