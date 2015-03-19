from server.models.db import db


class HowToResource(db.Model):
    __tablename__ = 'howto_resources'
    resource_id = db.Column(
        'resource_id',
        db.Integer,
        db.ForeignKey('resources.id'),
        primary_key=True)
    howto_id = db.Column(
        'howto_id', db.Integer, db.ForeignKey('howtos.id'), primary_key=True)

    howto = db.relationship('HowTo', backref=db.backref('howto_resource'))

    resource = db.relationship(
        'Resource', backref=db.backref('howto_resource'))

    def __init__(self, howto=None, resource=None):
        self.howto = howto
        self.resource = resource
