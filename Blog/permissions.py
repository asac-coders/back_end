from rest_framework import permissions


class Permission(permissions.BasePermission):
    def has_object_permission(self ,request, view , obj):
        
        if request.user.id == 1:
            return True
        if request.method == 'DELETE' and request.user.id !=1:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == obj.author:

            return True
    