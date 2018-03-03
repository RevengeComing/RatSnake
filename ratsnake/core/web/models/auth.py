import time
import bcrypt

from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin

from ratsnake.ext import db, login_manager

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

    class Meta:
        permissions = (
            ('can_get_groups', 'Can get groups'),
            ('can_add_groups', 'Can add groups'),
            ('can_edit_groups', 'Can edit groups'),
            ('can_delete_groups', 'Can delete groups'),
        )

    def add_permission(self, permission):
        perm = Permission.query.filter_by(code_name=permission).first()
        self.permissions.append(perm)

    def can(self, permission):
        if permission in [perm.code_name for perm in permissions]:
            return True
        return False


class GroupPermission(db.Model):
    __tablename__ = "rs_groups_permissions"
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('rs_groups.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('rs_permissions.id'))


class User(db.Model, UserMixin):
    __tablename__ = 'rs_users'
    id = db.Column(db.Integer, primary_key=True, index=True)

    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)

    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    group_id = db.Column(db.Integer, db.ForeignKey('rs_groups.id'))

    is_admin = db.Column(db.Boolean, default=False)
    is_staff = db.Column(db.Boolean, default=False)

    group = db.relationship(Group)

    class Meta:
        permissions = (
            ('can_get_users', 'Can get users'),
            ('can_add_users', 'Can add users'),
            ('can_edit_users', 'Can edit users'),
            ('can_delete_users', 'Can delete users'),
        )

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, _password):
        self.password_hash = bcrypt.hashpw(_password.encode('utf8'),
            bcrypt.gensalt()).decode()

    def check_password(self, _password):
        return bcrypt.checkpw(_password.encode('utf8'),
            self.password.encode('utf8'))

    def set_admin(self):
        self.is_admin = True
        self.is_staff = True

    def can(self, permission):
        if self.is_admin:
            return True
        return self.group.can(permission)


@login_manager.user_loader
def load_user(user_id):
    if current_app.config['SQLALCHEMY_DATABASE_URI']:
        return User.query.filter_by(id=user_id).first()
    return None


class AnonymousUser(AnonymousUserMixin):
    def can(self):
        return False

login_manager.anonymous_user = AnonymousUser