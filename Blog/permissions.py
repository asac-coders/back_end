from rest_framework import permissions

class PermissionsClass(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.student_number == request.user:
            return True