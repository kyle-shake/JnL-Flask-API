# from app import app, db
# from users import User, UserSchema, user_schema, users_schema

# def add_user(fname, lname, email, hash_password):
#     new_user = User(fname, lname, email, hash_password, 'User')

#     db.session.add(new_user)
#     db.session.commit()
#     return user_schema.jsonify(new_user)

# def get_users():
#     all_users = User.query.all()
#     result = users_schema.dump(all_users)
#     return jsonify(result)

# def login_user(email):
#     currUser = User.query.filter_by(emailAddress=email).first()
#     return user_schema.dump(currUser)



