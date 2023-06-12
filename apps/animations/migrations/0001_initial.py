# Generated by Django 3.2 on 2023-06-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='제목')),
            ],
            options={
                'verbose_name': '애니메이션',
                'db_table': 'animation',
            },
        ),
    ]
