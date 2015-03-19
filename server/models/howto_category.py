from server.models.db import db


class HowToCategory(db.Model):
    __tablename__ = 'howto_categories'
    category_id = db.Column(
        'category_id',
        db.Integer,
        db.ForeignKey('categories.id'),
        primary_key=True)
    howto_id = db.Column(
        'howto_id', db.Integer, db.ForeignKey('howtos.id'), primary_key=True)

    howto = db.relationship('HowTo', backref=db.backref('howto_category'))

    category = db.relationship(
        'Category', backref=db.backref('howto_category'))

    def __init__(self, howto=None, category=None):
        self.howto = howto
        self.category = category
