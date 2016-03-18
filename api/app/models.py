# bucketlist/models.py


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Initialise Flask
app = Flask(__name__)

db = SQLAlchemy(app)

class Bucketlist(db.Model):
    """Model for Bucketlist"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    date_created = db.Column(db.DateTime,
                             default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,
                              default=db.func.current_timestamp())
    created_by = db.Column(db.String(20))

    #  Constructor for Bucketlist
    def __init__(self, name, created_by):
        self.name = name
        self.created_by = created_by

    def __repr__(self):
        return '<Bucketlist %r>' % self.name


class BucketlistItem(db.Model):
    """Model for item in Bucketlist"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bucketlist = db.Column(db.Integer, db.ForeignKey('bucketlist.id'))
    bucketlist_id = db.relationship('Bucketlist', backref='items')
    date_created = db.Column(db.DateTime,
                             default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,
                              default=db.func.current_timestamp())
    done = db.Column(db.Boolean, default=False)

    #  Constructor for BucketlistItem
    def __init__(self, title, bucketlist):
        self.title = title
        self.bucketlist = bucketlist

    def __repr__(self):
        return '<Item %r>' % self.title


def initialise():
    """Initialize app by creating db and its dpendencies"""
    db.create_all()

def drop():
    """Delete db and its conten"""
    db.drop_all()