# groups/permissions.py

from rest_framework import permissions

class IsAdminOrMember(permissions.BasePermission):
    """
    Custom permission to only allow admins or members of the group to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow safe methods like GET
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow only the group creator (admin) or group members to modify group data
        return obj.created_by == request.user or request.user in obj.members.all()
