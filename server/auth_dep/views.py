# from flask import Blueprint, request, make_response, jsonify
# from flask.views import MethodView
# from werkzeug import generate_password_hash, check_password_hash

# from backend.server import bcrypt, db
# from backend.server.models.user import User, BlackListToken

# auth_blueprint = Blueprint('auth', __name__)

# class RegisterAPI(MethodView):
#     """
#     User Registration Resource
#     """
#     def post(self):
#         post_data = request.get_json()
#         user = User.query.filter_by(email=post_data.get('email')).first()
#         if not user:
#             try:
#                 user = User(
#                     fName=post_data.get('fName'),
#                     lName=post_data.get('lName'),
#                     email=post_data.get('email'),
#                     password=post_data.get('password'),
#                     admin=False
#                 )
#                 db.session.add(user)
#                 db.session.commit()
#                 auth_token = user.encode_auth_token(user.id)
#                 responseObject = {
#                     'status': 'success'
#                     'message': 'Successfully registered.'
#                     'auth_token': auth_token.decode()
#                 }
#                 return make_response(jsonify(responseObject)), 201
#             except Exception as e:
#                 responseObject = {
#                     'status': 'fail'
#                     'message': 'Some error occurred. Please try again'                    
#                 }
#                 return make_response(jsonify(responseObject)), 202

# class LoginAPI(MethodView):
#     """
#     User Login Resource
#     """
#     def post(self):
#         post_data = request.get_json()
#         try:
#             user = User.query.filter_by(
#                 email=post_data.get('email')
#             ).first()
#             if user and bcrypt.check_password_hash(
#                 user.password, post_data.get('password')
#             ):
#                 auth_token = user.encode_auth_token(user.id)
#                 if auth_token:
#                     responseObject = {
#                         'status': 'success'
#                         'message': 'Successfully logged in'
#                         'auth_token': auth_token.decode()
#                     }
#                     return make_response(jsonify(responseObject)), 200
#             else:
#                 responseObject = {
#                     'status': 'fail'
#                     'message': 'User does not exist'                     
#                 }
#                 return make_response(jsonify(responseObject)), 404
#         except Exception as e:
#             print(e)
#             responseObject = {
#                 'status': 'fail'
#                 'message': 'Try again'                     
#             }
#             return make_response(jsonify(responseObject)), 500

# class UserAPI(MethodView):
#     """
#     User Resource
#     """
#     def get(self):
#         auth_header = request.headers.get('Authorization')
#         if auth_header:
#             try:
#                 auth_token = auth_header.split(" ")[1]
#             except IndexError:
#                 responseObject = {
#                     'status': 'fail'
#                     'message': 'Bearer token malformed'
#                 }   
#                 return make_response(jsonify(responseObject)), 401
#         else:
#             auth_token = ''
#         if auth_token:
#             resp = User.decode_auth_token(auth_token)
#             if not isinstance(resp, str):
#                 user = User.query.filter_by(id=resp).first()
#                 responseObject = {
#                     'status': 'success'
#                     'data':{
#                         'user_id': user.id,
#                         'fName': user.fName,
#                         'lName': user.lName,
#                         'email': user.email,
#                         'admin': user.admin,
#                         'create_date': user.create_date
#                     }
#                 }
#                 return make_response(jsonify(responseObject)), 200
#             responseObject = {
#                 'status': 'fail'
#                 'message': resp
#             }
#             return make_response(jsonify(responseObject)), 401
#         else:
#             responseObject = {
#                 'status': 'fail',
#                 'message': 'Provide a valid auth token.'
#             }
#             return make_response(jsonify(responseObject)), 401

# class LogoutAPI(MethodView):
#     """
#     Logout Resource
#     """
#     def post(self):
#         auth_header = request.headers.get('Authorization')
#         if auth_header:
#             auth_token = auth_header.split(" ")[1]
#         else:
#             auth_token = ''
#         if auth_token:
#             resp = User.decode_auth_token(auth_token)
#             if not isinstance(resp, str):
#                 blacklist_token = BlackListToken(token=auth_token)
#                 try:
#                     db.session.add(blacklist_token)
#                     db.session.commit()
#                     responseObject = {
#                         'status': 'success',
#                         'message': 'Successfully logged out.'
#                     }
#                     return make_response(jsonify(responseObject)), 200
#                 except Exception as e:
#                     responseObject = {
#                         'status': 'fail',
#                         'message': e
#                     }
#                     return make_response(jsonify(responseObject)), 200
#             else:
#                 responseObject = {
#                     'status': 'fail',
#                     'message': resp
#                 }
#                 return make_response(jsonify(responseObject)), 401
#         else:
#             responseObject = {
#                 'status': 'fail',
#                 'message': 'Provide a valid auth token.'
#             }
#             return make_response(jsonify(responseObject)), 403

# # registration_view = RegisterAPI.as_view('register_api')
# # login_view = LoginAPI.as_view('login_api')
# # user_view = UserAPI.as_view('user_api')
# # logout_view = LogoutAPI.as_view('logout_api')

# # auth_blueprint.add_url_rule(
# #     '/auth/register',
# #     view_func=registration_view,
# #     methods=['POST']
# # )
# # auth_blueprint.add_url_rule(
# #     '/auth/login',
# #     view_func=login_view,
# #     methods=['POST']
# # )
# # auth_blueprint.add_url_rule(
# #     '/auth/status',
# #     view_func=user_view,
# #     methods=['GET']
# # )
# # auth_blueprint.add_url_rule(
# #     '/auth/logout',
# #     view_func=logout_view,
# #     methods=['POST']
# # )
