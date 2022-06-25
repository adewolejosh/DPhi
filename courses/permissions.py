from rest_framework.permissions import BasePermission

from accounts.models import UserExtension


class EducatorPerms(BasePermission):

    def has_permission(self, request, view):
        logged_user = request.user
        user = UserExtension.objects.get(user=logged_user)
        if user.category == "E":
            return True


class NonEducatorPerms(BasePermission):

    def has_permission(self, request, view):
        logged_user = request.user
        user = UserExtension.objects.get(user=logged_user)
        if user.category == "NE":
            return True


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


