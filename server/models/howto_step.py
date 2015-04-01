from server.models.db import db


class HowToStep(db.Model):
    __tablename__ = 'howto_steps'
    step_id = db.Column(
        'step_id',
        db.Integer,
        db.ForeignKey('steps.id'),
        primary_key=True)
    howto_id = db.Column(
        'howto_id', db.Integer, db.ForeignKey('howtos.id'), primary_key=True)

    howto = db.relationship('HowTo', backref=db.backref('howto_step'))
    step = db.relationship('Step', backref=db.backref('howto_step'))

    def __init__(self, howto=None, step=None):
        self.howto = howto
        self.step = step
