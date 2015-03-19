from server.models.db import db


class ResourceKeyword(db.Model):
    __tablename__ = 'resource_keywords'
    keyword_id = db.Column(
        'keyword_id',
        db.Integer,
        db.ForeignKey('keywords.id'),
        primary_key=True)
    resource_id = db.Column(
        'resource_id',
        db.Integer,
        db.ForeignKey('resources.id'),
        primary_key=True)

    resource = db.relationship(
        'Resource', backref=db.backref('resource_keyword'))
    keyword = db.relationship(
        'Keyword', backref=db.backref('resource_keyword'))

    def __init__(self, resource=None, keyword=None):
        self.resource = resource
        self.keyword = keyword
