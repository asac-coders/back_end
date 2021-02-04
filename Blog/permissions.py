from rest_framework import permissions

class PermissionsClass(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if obj.student_number != 1 and request.method == 'POST':
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.id == 1:
            return True
        if obj.student_number == request.user:
            return True