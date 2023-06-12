
from django.db import models

from apps.accounts.models import User
from apps.animations.models import Animation


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    animation = models.ForeignKey(Animation, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField('내용')
    like = models.ManyToManyField(User, through='CommentLike', related_name='liked_comments')

    class Meta:
        db_table = 'comment'
        verbose_name = '댓글'

    def get_likes_count(self):
        return self.like.count()


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment_like'
        verbose_name = '댓글 좋아요'