#backend/server/resources/post.py
import json
import werkzeug, os

from flask import make_response, request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from server.models.post_models import Post, post_schema, posts_schema

UPLOAD_FOLDER = 'static/img'

class PostsAPI(Resource):
    def get(self):
        posts = Post.query.all()
        results = posts_schema.dump(posts)
        return jsonify(results)

    @jwt_required
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        imageFile = args['file']
        path = ""
        if imageFile:
            path = os.path.join(UPLOAD_FOLDER, 'postpic_test.png')
            imageFile.save(path)
        author = args['author']
        post_data = request.get_json()
        new_post = Post(
            author = post_data.get("author"),            
            title=post_data.get("title"),
            content=post_data.get("content"),
            pinned=post_data.get("pinned")
        )
        new_post = new_post.create()
        result = post_schema.dump(new_post)
        return result, 200

class PostAPI(Resource):
    @jwt_required
    def put(self, id):
        put_data = request.get_json()
        post = Post.query.get(id)
        post = post.update(put_data)
        result = post_schema.dump(post)
        return result, 200

    @jwt_required
    def delete(self, id):
        post = Post.query.get(id)
        post.delete()
        return '', 204

    def get(self, id):
        post = Post.query.get(id)
        result = post_schema.dump(post)
        return result, 200