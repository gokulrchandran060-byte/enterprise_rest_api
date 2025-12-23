from rest_framework.permissions import BasePermission

class CanViewAllMessages(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("core.can_view_all_messages")