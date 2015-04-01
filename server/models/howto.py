"""This module contains the HowTo class."""
from server.models.db import db


class HowTo(db.Model):

    """SQLAlchemy model definition for the event class."""

    __tablename__ = 'howtos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    is_approved = db.Column(db.Boolean)

    resources = db.relationship('Resource', secondary='howto_resources')
    categories = db.relationship('Category', secondary='howto_categories')
    keywords = db.relationship('Keyword', secondary='howto_keywords')
