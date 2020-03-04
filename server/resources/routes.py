from .event import EventsAPI, EventAPI
from .auth import RegisterAPI, LoginAPI
from .post import PostAPI, PostsAPI
from .media import PhotoAPI, PhotosAPI, VideoAPI, VideosAPI

def init_routes(api):
    api.add_resource(RegisterAPI, '/api/register')
    api.add_resource(LoginAPI, '/api/login')
    api.add_resource(EventsAPI, '/api/events')
    api.add_resource(EventAPI, '/api/event/<id>')
    api.add_resource(PostsAPI, '/api/posts')
    api.add_resource(PostAPI, '/api/post/<id>')
    api.add_resource(PhotosAPI, '/api/photos')
    api.add_resource(PhotoAPI, '/api/photo/<id>')
    api.add_resource(VideosAPI, '/api/videos')
    api.add_resource(VideoAPI, '/api/video/<id>')