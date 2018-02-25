from ratsnake.ext import db

__all__ = ['Option']


class Option(db.Model):
    __tablename__ = 'rs_options'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    value = db.Column(db.Text)