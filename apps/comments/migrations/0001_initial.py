# Generated by Django 3.2 on 2023-06-12 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('report_cnt', models.IntegerField(default=0, verbose_name='댓글 신고 갯수')),
                ('animation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='animations.animation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '댓글',
                'db_table': 'comment',
            },
        ),
    ]
