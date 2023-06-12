
from django.db import models

from apps.accounts.models import User
from apps.animations.models import Animation


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    animation = models.ForeignKey(Animation, on_delete=models.CASCADE, related_name='comments')

    content = models.TextField('내용')

    class Meta:
        db_table = 'comment'
        verbose_name = '댓글'
