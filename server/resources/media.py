#backend/server/resources/media.py
import json
import werkzeug, os

from flask import make_response, request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from server.models.media_models import Photo, photo_schema, photos_schema, Video, video_schema, videos_schema

UPLOAD_FOLDER = 'static/img'

class PhotosAPI(Resource):
    def get(self):
        photos = Photo.query.all()
        results = photos_schema.dump(photos)
        return jsonify(results)

    @jwt_required
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')                
        args = parse.parse_args()
        if args['file'] == "":
            return {
                'data':'',
                'message': 'No File Provided',
                'status': 'error'
            }
        imageFile = args['file']
        if imageFile:
            path = os.path.join(UPLOAD_FOLDER, 'test.png')
            imageFile.save(path)
            tdate = None
            if(args['tdate']):
                tdate=args['taken_date']
            physloc = None
            if(args['physloc']):
                physloc = args['physloc']
            desc = None
            if(args['desc']):
                desc = args['desc']
            categories = None
            if(args['categories']):
                categories = args['categories']
            new_photo = Photo(
                tdate=tdate,
                path=path,
                physloc=physloc,
                desc=desc,
                categories=categories
            )
            new_photo = new_photo.create()
            id = new_photo.id
            return make_response(jsonify({'id': str(id)})), 200

class PhotoAPI(Resource):
    @jwt_required
    def put(self, id):
        put_data = request.get_json()
        photo = Photo.query.get(id)
        photo = photo.update(put_date)
        result = photo_schema.dump(photo)
        return jsonify(result), 200

    @jwt_required
    def delete(self, id):
        photo = Photo.query.get(id)
        pathToImg = photo.path
        if(os.path.isfile(pathToImg)):
            photo.delete()
            os.remove(pathToImg)
        return '', 204

    def get(self, id):
        photo = Photo.query.get(id)
        result = photo_schema.dump(photo)
        return result, 200

class VideosAPI(Resource):
    def get(self):
        videos = Video.query.all()
        results = videos_schema.dump(videos)
        return jsonify(results)

    @jwt_required
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        if(args['file']== ""):
            return {
                'data': '',
                'message': 'No File Provided',
                'status': 'error'
            }
        videoFile = args['file']
        if videoFile:
            path = os.path.join(UPLOAD_FOLDER, 'test.mp4')
            videoFile.save(path)            
            tdate = None
            if(args['tdate']):
                tdate=args['taken_date']
            physloc = None
            if(args['physloc']):
                physloc = args['physloc']
            desc = None
            if(args['desc']):
                desc = args['desc']
            categories = None
            if(args['categories']):
                categories = args['categories']
            ytlink = None
            if(args['ytlink']):
                ytlink = args['ytlink']
            new_video = Video(
                tdate=tdate,
                path=path,
                physloc=physloc,
                desc=desc,
                categories=categories,
                ytlink=ytlink
            )
            new_video = new_video.create()
            id = new_video.id
            return make_response(jsonify({'id': str(id)})), 200

class VideoAPI(Resource):
    @jwt_required
    def put(self, id):
        put_data = request.get_json()
        video = Video.query.get(id)
        video = video.update(put_date)
        result = video_schema.dump(video)
        return jsonify(result), 200

    @jwt_required
    def delete(self, id):
        video = Video.query.get(id)
        pathToVid = video.path
        if(os.path.isfile(pathToVid)):
            video.delete()
            videoFile = os.remove(pathToVid)
        return '', 204

    def get(self, id):
        video = Video.query.get(id)
        result = video_schema.dump(video)
        return result, 200