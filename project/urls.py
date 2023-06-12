from django.urls import path, include
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularYAMLAPIView, SpectacularSwaggerView, \
    SpectacularRedocView

from project import settings

urlpatterns = [
    path("reports/", include("apps.reports.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("comments/", include("apps.comments.urls")),

]


if settings.DEBUG:

    urlpatterns += [
        # Open API 자체를 조회 : json, yaml,
        path("json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
        path("yaml/", SpectacularYAMLAPIView.as_view(), name="swagger-yaml"),
        # Open API Document UI로 조회: Swagger, Redoc
        path(
            "swagger/",
            SpectacularSwaggerView.as_view(url_name="schema-json"),
            name="swagger-ui",
        ),
        path(
            "redoc/",
            SpectacularRedocView.as_view(url_name="schema-json"),
            name="redoc",
        ),
    ]