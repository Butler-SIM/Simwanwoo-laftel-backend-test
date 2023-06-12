from django.db.models import Prefetch
from rest_framework import  viewsets, mixins
from rest_framework.pagination import BasePagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer, CommentCreateSerializer, CommentUpdateSerializer
from common.permission import IsCommentAuthorOrReadOnly


class CommentViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by("-id")
    pagination_class = BasePagination

    def get_serializer_class(self):
        if self.action == "create":
            return CommentCreateSerializer

        if self.action in ("update", "partial_update"):
            return CommentUpdateSerializer

        return CommentSerializer

    def get_permissions(self):
        permission_classes = self.permission_classes
        if self.action in ("update", "partial_update"):
            permission_classes = [IsCommentAuthorOrReadOnly]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "list":
            queryset = (
                self.queryset.prefetch_related(
                    "user",
                )

            )

        if self.action in ("update", "partial_update"):
            queryset = queryset.filter(state="ACTIVE")

        return queryset



