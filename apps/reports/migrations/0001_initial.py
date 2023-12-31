# Generated by Django 3.2 on 2023-06-12 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0002_remove_comment_report_cnt'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('ADVERTISEMENT', 'ADVERTISEMENT'), ('SPAM', 'SPAM'), ('ABUSE', 'ABUSE'), ('PORN', 'PORN'), ('SPOILER', 'SPOILER')], max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'report',
                'ordering': ['-created_date'],
            },
        ),
    ]
