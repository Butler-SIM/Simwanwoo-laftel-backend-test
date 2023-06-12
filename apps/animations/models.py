from django.db import models

class Animation(models.Model):

    title = models.CharField('제목', max_length=256)

    class Meta:
        db_table = 'animation'
        verbose_name = '애니메이션'
