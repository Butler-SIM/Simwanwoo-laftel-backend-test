from django.urls import path
from apps.reports.views import post_report

app_name = "api.reports"

urlpatterns = [
    path("", post_report, name="reports"),
]
