from server.models.db import db


class HowToKeyword(db.Model):
    __tablename__ = 'howto_keywords'
    keyword_id = db.Column(
        'keyword_id',
        db.Integer,
        db.ForeignKey('keywords.id'),
        primary_key=True)
    howto_id = db.Column(
        'howto_id', db.Integer, db.ForeignKey('howtos.id'), primary_key=True)

    howto = db.relationship('HowTo', backref=db.backref('howto_keyword'))
    keyword = db.relationship('Keyword', backref=db.backref('howto_keyword'))

    def __init__(self, howto=None, keyword=None):
        self.howto = howto
        self.keyword = keyword
