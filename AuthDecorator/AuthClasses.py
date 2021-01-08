from rest_framework.permissions import BasePermission
from .decorators import is_driver


class IsDriver(BasePermission):
    def has_permission(self, request, view):
        return is_driver(request.user)
