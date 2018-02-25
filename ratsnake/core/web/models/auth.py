import time

from ratsnake.ext import db

# __all__ = ['User']

def create_groups():
    Permission.create_basic_permissions()
    Group.create_admin_group()


class Permission(db.Model):
    __tablename__ = "rs_permissions"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64))
    code_name = db.Column(db.String(64), index=True)

    groups = db.relationship('Group', secondary='rs_groups_permissions')


class Group(db.Model):
    __tablename__ = "rs_groups"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64))

    permissions = db.relationship('Permission', secondary='rs_groups_permissions')

    def add_permission(self, permission):
        perm = Permission.query.filter_by(code_name=permission).first()
        self.permissions.append(perm)


class GroupPermission(db.Model):
    __tablename__ = "rs_groups_permissions"
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('rs_groups.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('rs_permissions.id'))


class User(db.Model):
    __tablename__ = 'rs_users'
    id = db.Column(db.Integer, primary_key=True, index=True)

    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64))

    email = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(128))

    group_id = db.Column(db.Integer, db.ForeignKey('rs_groups.id'))

    is_admin = db.Column(db.Boolean, default=False)