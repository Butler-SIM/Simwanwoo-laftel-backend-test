from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.comments.views import CommentViewSet, like_post, like_delete

app_name = "apps.comments"

router = DefaultRouter(trailing_slash=False)
router.register(r"", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "<int:id>/like",
        like_post,
        name="comment_like",
    ),
    path(
        "<int:id>/un-like",
        like_delete,
        name="comment_un_like",
    ),
]
