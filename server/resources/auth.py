#backend/server/resources/auth.py
import datetime

from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from server.models.user_models import User, user_schema


class RegisterAPI(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('email', required=True)
        parse.add_argument('fName')
        parse.add_argument('lName')
        parse.add_argument('password')
        parse.add_argument('fbID')
        args = parse.parse_args()
        if args['email'] == "":
            return {
                'data': '',
                'message': 'Invalid Registration. No Email',
                'status': 'error'
            }
        user = User.query.filter_by(emailAddress=args['email']).first()
        if not user:
            if args['password'] == "" and args['fbID'] == "":
                return {
                    'data': '',
                    'message': "Invalid Registration. No Password or Facebook ID",
                    'status': 'error'
                }
            try:
                user = User(
                    fName=args['fName'],
                    lName=args['lName'],
                    email=args['email'],
                    password=args['password'],
                    fbID=args['fbID'],
                    admin=False
                )
                if args['password'] != "":
                    user.hash_password()

                user = user.create()
                userData = user_schema.dump(user)
                expires = datetime.timedelta(days=7)
                access_token = create_access_token(identity=str(user.id), expires_delta=expires)
                responseObject = {
                        'data': userData,
                        'status': 'success',
                        'message': 'Successfully registered.',
                        'token': access_token
                    }
                return responseObject, 201
            except Exception as e:
                responseObject = {
                    'data': '',
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again'                    
                }
                return responseObject, 202

class LoginAPI(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("email", required=True)
        parse.add_argument("password")
        parse.add_argument("fbID")
        args = parse.parse_args()
        if args["email"] == "":
            return {
                "data":"",
                "message": "Login Failed. No Email Provided",
                "status": "error"
            }
        try:
            user = User.query.filter_by(
                emailAddress=args['email']
            ).first()
            
            if user:
                userData = user_schema.dump(user)
                authorized = False
                if user.password:
                    authorized = user.check_password(args['password'])
                if user.facebookUserID:
                    authorized = user.facebookUserID == args['fbID']

                if authorized:
                    expire_date = datetime.timedelta(days=7)
                    access_token = create_access_token(identity=str(user.id), expires_delta=expire_date)
                    if access_token:
                        responseObject = {
                            'data': userData,
                            'status': 'success',
                            'message': 'Successfully logged in',                            
                            'token': access_token
                        }
                        return responseObject, 200
                else:
                    responseObject = {
                        'data': '',
                        'status': 'fail',
                        'message': 'Incorrect Password or Facebook ID'                     
                    }
                    return responseObject, 404
            else:
                responseObject = {
                    'data': '',
                    'status': 'fail',
                    'message': 'User does not exist'                     
                }
                return responseObject, 404
        except Exception as e:
            print(e)
            responseObject = {
                'data': '',
                'status': 'fail',
                'message': 'Try again'                     
            }
            return responseObject, 500
            