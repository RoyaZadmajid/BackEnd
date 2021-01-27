from rest_framework import permissions


class IsAdminStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return any([user.is_superuser, user.is_staff])
