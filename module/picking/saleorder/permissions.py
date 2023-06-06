from rest_framework import permissions


class IsCompanyObject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        company = obj.company
        return user.company == company
