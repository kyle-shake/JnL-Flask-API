import datetime
from server.database.db import db, ma

#Photo Class
class Photo(db.Model):
    __tablename__ = "photos"

    id = db.Column("photo_id", db.Integer, primary_key=True, autoincrement=True)
    udate = db.Column("upload_date", db.DateTime, nullable=False)
    tdate = db.Column("taken_date", db.DateTime)
    path = db.Column("img_path", db.Text, nullable=False)
    physloc = db.Column("physical_location", db.String(50))
    desc = db.Column("description", db.Text)
    categories = db.Column(db.Text)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, newData):
        self.data = newData
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, tdate, path, physloc, desc, categories):
        self.udate = datetime.datetime.now()
        self.tdate = tdate
        self.path = path
        self.physloc = physloc
        self.desc = desc
        self.categories = categories

    def __repr__(self):
        return '' % self.path

class PhotoSchema(ma.Schema):
    class Meta:
        fields = ("id", "udate", "tdate", "path", "physloc", "desc", "categories")

photo_schema = PhotoSchema()
photos_schema = PhotoSchema(many=True)

#Video Class
class Video(db.Model):
    __tablename__ = "videos"

    id = db.Column("video_id", db.Integer, primary_key=True, autoincrement=True)
    udate = db.Column("upload_date", db.DateTime, nullable=False)
    tdate = db.Column("taken_date", db.DateTime)
    path = db.Column("video_path", db.Text, nullable=False)
    physloc = db.Column("physical_location", db.String(50))
    desc = db.Column("description", db.Text)
    categories = db.Column(db.Text)
    ytlink = db.Column("youtube_link", db.String(50))

    def __init__(self, tdate, path, physloc, desc, categories, ytlink):
        self.udate = datetime.datetime.now()
        self.tdate = tdate
        self.path = path
        self.physloc = physloc
        self.desc = desc
        self.categories = categories
        self.ytlink = ytlink

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, newData):
        self.data = newData
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '' % self.path

class VideoSchema(ma.Schema):
    class Meta:
        fields = ("id", "udate", "tdate", "path", "physloc", "desc", "categories", "ytlink")

video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)