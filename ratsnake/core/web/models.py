import time

from ratsnake.ext import db


class Permission:
    USE = 0x01
    WRITE = 0x02
    ADMINISTER = 0x80


roles = {
    'User': (Permission.USE , True),
    'Writer': (Permission.USE | Permission.WRITE, False),
    'Administrator': (0xff, False)
}


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='joined')

    @staticmethod
    def insert_roles():      
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()


class User(db.Model):
    __tablename__ = "rs_users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.Integer, default=time.time())