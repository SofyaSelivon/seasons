# Generated by Django 5.2.1 on 2025-05-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0002_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='dislikes_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='season',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
