from server.database.db import db, ma

#Event Class
class Event(db.Model):
    __tablename__ = "events"

    id = db.Column("Event_ID", db.Integer, primary_key=True, autoincrement=True)
    edate = db.Column("Event_Date", db.DateTime, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column("Description", db.Text, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    fblink = db.Column("FB_Link", db.String(50), nullable=False)

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

    def __init__(self, edate, title, description, location, fblink):
        self.edate = edate
        self.title = title
        self.desc = description
        self.location = location
        self.fblink = fblink
    
    def __repr__(self):
        return '' % self.id

class EventSchema(ma.Schema):
    class Meta:
        fields = ("id", "edate", "title", "desc", "location", "fblink")

event_schema = EventSchema()
events_schema = EventSchema(many=True)