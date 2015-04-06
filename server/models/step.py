"""This module contains the Step class."""
from server.models.db import db


class Step(db.Model):

    """SQLAlchemy model definition for the event class."""

    __tablename__ = 'steps'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)
