from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.reports.models import Report
from apps.reports.schemas import ReportSchema
from apps.reports.serializers import ReportOnlySerializer


@ReportSchema.report_schema
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_report(request, *args, **kwargs):
    """댓글 신고"""

    comment_id = request.data.get('comment')

    if not Report.objects.filter(comment=comment_id, user=request.user).exists():
        report = Report.objects.create(
            comment_id=comment_id,
            reason=request.data.get("reason"),
            user=request.user,
        )
        return Response(
            ReportOnlySerializer(report).data,
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"Error": "이미 신고한 댓글, 대댓글입니다"},
            status=status.HTTP_400_BAD_REQUEST,
        )
