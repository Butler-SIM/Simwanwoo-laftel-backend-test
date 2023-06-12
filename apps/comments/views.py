from django.db.models import Prefetch, Count, Q
from rest_framework import  viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.comments.models import Comment
from apps.comments.schemas import CommentSchema
from apps.comments.serializers import CommentSerializer, CommentCreateSerializer, CommentUpdateSerializer
from common.permission import IsCommentAuthorOrReadOnly


@CommentSchema.comment_schema_view
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
    pagination_class = PageNumberPagination
    filterset_fields = ["animation_id"]

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

            ).annotate(
                report_cnt=Count(
                    "report",
                    filter=~Q(report__reason="SPOILER"),
                )
            ).annotate(
                spoiler_report_cnt=Count(
                    "report",
                    filter=Q(report__reason="SPOILER"),
                )
            ).exclude(
                report_cnt__gte=3
            )

        if self.action in ("update", "partial_update"):
            queryset = queryset.filter(state="ACTIVE")

        return queryset


