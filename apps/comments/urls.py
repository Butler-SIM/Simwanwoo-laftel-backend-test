from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.comments.views import CommentViewSet

app_name = "apps.comments"

router = DefaultRouter(trailing_slash=False)
router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(router.urls)),
]
