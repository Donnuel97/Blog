# Generated by Django 4.0.4 on 2022-05-26 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_comment_approved_comment_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
    ]
