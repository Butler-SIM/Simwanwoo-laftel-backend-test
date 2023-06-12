from rest_framework import permissions


class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    """작성자만 수정,삭제 가능 권한"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
