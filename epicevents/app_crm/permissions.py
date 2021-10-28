from rest_framework import permissions
from . import models

class ProspectPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.role in ('MANAGER', 'COMMERCIAL')
        elif request.method == 'PUT':
            return request.user.role == 'COMMERCIAL'
        return request.user.role == 'MANAGER'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.role in ('MANAGER', 'COMMERCIAL')
        return request.user.role == 'MANAGER'


class ClientPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'COMMERCIAL'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.pk == obj.sale_contact


class ContractPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'COMMERCIAL'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj in models.Contract.objects.filter(
            event__support_contact=request.user.pk)


class EventPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'COMMERCIAL'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.pk == obj.support_contact
