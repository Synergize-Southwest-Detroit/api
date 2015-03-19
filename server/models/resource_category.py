from server.models.db import db


class ResourceCategory(db.Model):
    __tablename__ = 'resource_categories'
    category_id = db.Column(
        'category_id',
        db.Integer,
        db.ForeignKey('categories.id'),
        primary_key=True)
    resource_id = db.Column(
        'resource_id',
        db.Integer,
        db.ForeignKey('resources.id'),
        primary_key=True
    )

    resource = db.relationship(
        'Resource', backref=db.backref('resource_category'))

    category = db.relationship(
        'Category', backref=db.backref('resource_category'))

    def __init__(self, resource=None, category=None):
        self.resource = resource
        self.category = category
