from django.urls import path
from apps.reports.views import post_report

app_name = "apps.reports"

urlpatterns = [
    path("", post_report, name="reports"),
]
