from django.db import models

from apps.accounts.models import User
from apps.comments.models import Comment


class Report(models.Model):
    """
    Report
    """
    reason = (
        ("ADVERTISEMENT", "ADVERTISEMENT"),  # 광고/홍보게시물
        ("SPAM", "SPAM"),  # 도배게시물
        ("ABUSE", "ABUSE"),  # 욕설/혐오/차별적 표현
        ("PORN", "PORN"),  # 음란게시물
        ("SPOILER", "SPOILER")    # 스포일러
    )

    reason = models.CharField(max_length=20, choices=reason)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "report"
        ordering = ["-created_date"]
