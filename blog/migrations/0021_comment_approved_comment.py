# Generated by Django 4.0.4 on 2022-07-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_profile_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]