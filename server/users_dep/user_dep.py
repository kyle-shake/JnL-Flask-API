# import datetime
# import jwt

# from backend.server import app, db, bcrypt

# #User Class
# class User(db.Model):
#     __tablename__ = "users"

#     id = db.Column("user_id", db.Integer, primary_key=True, autoincrement=True)
#     firstName = db.Column("firstName", db.String(45), nullable=False)
#     lastName = db.Column("lastName", db.String(45), nullable=False)
#     emailAddress = db.Column("emailAddress", db.String(45), unique=True, nullable=False)
#     password = db.Column("password", db.String(45), nullable=False)
#     admin = db.Column("admin", db.Boolean, nullable=False)    
#     create_date = db.Column("create_date", db.DateTime, nullable=False)

#     def __init__(self, fName, lName, email, password, admin):
#         self.firstName = fName
#         self.lastName = lName
#         self.emailAddress = email
#         self.password = password
#         self.admin = admin
#         self.create_date = datetime.datetime.now()

#     def encode_auth_token(self, user_id):
#         """
#         Generates the Auth Token
#         """
#         try:
#             payload = {
#                 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
#                 'iat': datetime.datetime.utcnow(),
#                 'sub': user_id
#             }
#             return jwt.encode(
#                 payload,
#                 app.config.get('SECRET_KEY'),
#                 algorithm='HS256'
#             )
#         except Exception as e:
#             return e

#     @staticmethod
#     def decode_auth_token(auth_token):
#         """
#         Validates the auth token
#         :param auth_token:
#         :return: integer|string
#         """
#         try:
#             payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
#             is_blacklisted_token = BlackListToken.check_blacklist(auth_token)


# class BlackListToken(db.Model):
#     """
#     Token Model for storing JWT tokens
#     """
#     __tablename__ = 'blacklist_tokens'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     token = db.Column(db.String(500), unique=True, nullable=False)
#     blacklisted_on = db.Column(db.DateTime, nullable=False)

#     def __init__(self, token):
#         self.token = token
#         self.blacklisted_on = datetime.datetime.now()

#     def __repr__(self):
#         return '<id: token: {}'.format(self.token)

#     @staticmethod
#     def check_blacklist(auth_token):
#         res = BlackListToken.query.filter_by(token=str(auth_token)).first()
#         if res:
#             return True
#         else:
#             return False
