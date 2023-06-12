from rest_framework import serializers
from apps.reports.models import Report


class ReportOnlySerializer(serializers.ModelSerializer):
    """ReportCreate  Serializer"""

    class Meta:
        model = Report
        fields = "__all__"


class ReportCreateSerializer(serializers.ModelSerializer):
    """ReportCreate  Serializer"""

    class Meta:
        model = Report
        fields = [
            "comment",
            "reason",
        ]
