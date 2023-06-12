from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

from apps.reports.serializers import ReportCreateSerializer


TAG = "api-reports"


class ReportSchema:
    report_schema = extend_schema(
        tags=[TAG],
        summary=f"댓글 신고 ",
        description="""
        댓글신고
        reason = (
        ("ADVERTISEMENT", "ADVERTISEMENT"),  # 광고/홍보게시물
        ("SPAM", "SPAM"),  # 도배게시물
        ("ABUSE", "ABUSE"),  # 욕설/혐오/차별적 표현
        ("PORN", "PORN"),  # 음란게시물
        ("SPOILER", "SPOILER")    # 스포일러
    )
        """,

        request=ReportCreateSerializer,
    )
