"""This module contains the SQLAlchemy user class definition."""
from flask_login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy
from server.models.db import db


class User(db.Model, UserMixin):

    """SQLAlchemy user class definition."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(50), unique=True)
    password = db.Column('password', db.String(50))
    is_admin = db.Column('is_admin', db.Boolean)

    favorites = association_proxy('event_favorite', 'event')

    def __init__(self, username, password, is_admin):
        """Constructor for user."""
        self.username = username
        self.password = password
        self.is_admin = is_admin
