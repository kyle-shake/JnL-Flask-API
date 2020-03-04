#backend/server/resources/event.py
import json

from flask import make_response, request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from server.models.event_models import Event, events_schema, event_schema


class EventsAPI(Resource):
    def get(self):
        events = Event.query.all()
        results = events_schema.dump(events)        
        return jsonify(results)
    
    @jwt_required
    def post(self):
        post_data = request.get_json()
        new_event = Event(
            edate=post_data.get("eDate"),
            title=post_data.get("title"),
            description=post_data.get("description"),
            location=post_data.get("location"),
            fblink=post_data.get("fb_link")            
        )
        new_event = new_event.create()
        id = new_event.id
        return make_response(jsonify({'id': str(id) })), 200

class EventAPI(Resource):

    @jwt_required
    def put(self, id):
        put_data = request.get_json()
        event = Event.query.get(id)
        event = event.update(put_data)
        result = event_schema.dump(event)
        return jsonify(result), 200

    @jwt_required
    def delete(self, id):
        event = Event.query.get(id)
        event.delete()
        return '', 204

    def get(self, id):
        event = Event.query.get(id)
        result = event_schema.dump(event)
        return result, 200
