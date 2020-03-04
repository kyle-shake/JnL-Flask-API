from server.database.db import db, ma

#Post Class
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column("post_id", db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(50), nullable=False)
    pdate = db.Column("post_date", db.DateTime, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pinned = db.Column(db.Boolean, nullable=False)
    imgFilePath = db.Column(db.Text, nullable=True)

    def __init__(self, author, title, content, pinned, path):
        self.author = author
        self.pdate = datetime.datetime.now()
        self.title = title
        self.content = content
        self.pinned = pinned
        self.imgFilePath = path

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
        return '' % self.title

class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "author", "pdate", "title", "content", "pinned", "imgFilePath")

post_schema = PostSchema()
posts_schema = PostSchema(many=True)