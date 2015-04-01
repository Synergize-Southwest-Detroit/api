"""This module contains the Event class."""
from server.models.db import db


class Event(db.Model):

    """SQLAlchemy model definition for the event class."""

    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    address = db.Column(db.Text)
    display_address = db.Column(db.Text)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)

    categories = db.relationship('Category', secondary='event_categories')
