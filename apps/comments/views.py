from django.db.models import Prefetch, Count, Q
from django.shortcuts import get_object_or_404
from rest_framework import  viewsets, mixins
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from apps.comments.models import Comment
from apps.comments.schemas import CommentSchema, LikeSchema
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

        if self.action in ("like", "un_like"):
            return CommentCreateSerializer

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
            ).annotate(
                like_count=Count(
                    "like", distinct=True
                                 )
            ).exclude(
                report_cnt__gte=3
            )

        if self.action in ("update", "partial_update"):
            queryset = queryset.filter(state="ACTIVE")

        return queryset


@LikeSchema.article_like_schema
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_post(request, **kwargs):
    comment = get_object_or_404(Comment, id=kwargs.get("id"))

    if comment.like.filter(id=request.user.id).exists():
        raise ValidationError(
            {"already like": "a comment that has already clicked like"}
        )

    comment.like.add(request.user.id)

    return Response(
        {
            "success": "like",
            "comment_id": comment.id,
        },
        status=201,
    )


@LikeSchema.article_like_schema
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def like_delete(request, **kwargs):
    comment = get_object_or_404(Comment, id=kwargs.get("id"))

    if not comment.like.filter(id=request.user.id).exists():
        raise ValidationError(
            {"already delete like": "a comment that has already delete like"}
        )

    comment.like.remove(request.user.id)

    return Response(
        {
            "success": "un_like",
            "comment_id": comment.id,
        },
        status=204,
    )
