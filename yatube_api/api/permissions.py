from rest_framework import permissions, status


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = "У вас нет прав на изменения!"
    code = status.HTTP_403_FORBIDDEN

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        if (request.user != obj.author
           and request.method in permissions.SAFE_METHODS):
            return True

        if request.user == obj.author:
            return True
        return False
