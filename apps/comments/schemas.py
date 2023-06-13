from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)

from apps.comments.serializers import CommentSerializer, CommentCreateSerializer, CommentUpdateSerializer


class CommentSchema:
    tag = "comments"
    comment_list_schema = extend_schema(
        tags=[tag],
        summary=f"- 댓글 목록 조회 API_UPDATE : 2023-06-12",
        parameters=[
            OpenApiParameter(
                name="page_size",
                description=f"page_size 기본값 10.",
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name="animation_id",
                description="animation id값 필수 입력",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="is_my_comments",
                description="is_my_comments 내 댓글만 보기(true, false)",
                required=False,
                type=bool,
            ),
            OpenApiParameter(
                name="ordering",
                description="ordering_fields['like_count', 'id']",
                required=False,
                type=str,
            ),
        ],

        responses=CommentSerializer,
    )

    comment_create_schema = extend_schema(
        tags=[tag],
        summary=f"생성 API_UPDATE : 2023-06-12",
        request=CommentCreateSerializer,
        responses=CommentCreateSerializer,
    )

    comment_detail_schema = extend_schema(
        tags=[tag],
        summary=f"댓글 상세 조회 API_UPDATE : 2023-06-12",
        responses=CommentSerializer,
    )

    comment_detail_update_schema = extend_schema(
        tags=[tag],
        summary=f"댓글 수정 API_UPDATE : 2023-06-12",
        description="댓글 수정\n\n작성자만 수정 가능합니다.",
        request=CommentUpdateSerializer,
        responses=CommentUpdateSerializer,
    )

    comment_schema_view = extend_schema_view(
        list=comment_list_schema,
        create=comment_create_schema,
        retrieve=comment_detail_schema,
        update=comment_detail_update_schema,
        partial_update=comment_detail_update_schema,
    )


class LikeSchema:
    tag = "'comments-like'"
    article_like_schema = extend_schema(
        tags=[tag],
        summary=f"댓글 좋아요",
        description="좋아요",
    )
    article_like_delete_schema = extend_schema(
        tags=[tag],
        summary=f"좋아요 삭제",
        description="좋아요 삭제",
    )

    article_like_schema_view = extend_schema_view(
        like_post=article_like_schema, like_delete=article_like_delete_schema
    )

