from flask import jsonify
from flask_restful import Resource, Api

from ratsnake import staff_required_rest, admin_required_rest, permission_required

from . import panel
from ..models import sidebar_links, add_sidebar_link, sidebar_link

panel_api = Api(panel)


class BaseResource(Resource):

    def get(self, *args, **kwargs):
        abort(405)

    def post(self, *args, **kwargs):
        abort(405)

    def put(self, *args, **kwargs):
        abort(405)

    def patch(self, *args, **kwargs):
        abort(405)

    def delete(self, *args, **kwargs):
        abort(405)


class PanelResource(BaseResource):
    # method_decorators = [staff_required_rest]
    pass


def rest_resource(resource_cls):
    """ Decorator for adding resources to Api App """
    panel_api.add_resource(resource_cls, *resource_cls.endpoints)
    return resource_cls


@rest_resource
class DashboardApi(PanelResource):
    endpoints = ['/api/dashboard/']

    def get(self):
        pass


@rest_resource
class SidebarApi(PanelResource):
    endpoints = ['/api/sidebar-links/']

    def get(self):
        return sidebar_links.jsonify()


@sidebar_link('Users')
@rest_resource
class UserApi(PanelResource):
    sidebar_endpoint = '/api/users/'
    endpoints = ['/api/users/', '/api/users/<user_id>/']
    method_decorators = {
        'get': [permission_required('can_get_users')],
        'post': [permission_required('can_add_users')],
        'delete': [permission_required('can_delete_users')],
        'put': [permission_required('can_update_users')],
    }

    def get(self, user_id=None):
        return "siktir"
