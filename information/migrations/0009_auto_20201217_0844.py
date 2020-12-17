# Generated by Django 3.1.3 on 2020-12-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0008_comment_review_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='review_image',
        ),
        migrations.AddField(
            model_name='information',
            name='place',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='timedate',
            field=models.TextField(null=True),
        ),
    ]
