from server.models.db import db


class Resource(db.Model):
    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    resource = db.Column(db.String(128))
    is_approved = db.Column(db.Boolean)

    howtos = db.relationship('HowTo', secondary='howto_resources')
    categories = db.relationship('Category', secondary='resource_categories')
    keywords = db.relationship('Keyword', secondary='resource_keywords')
