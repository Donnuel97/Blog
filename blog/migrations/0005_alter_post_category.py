# Generated by Django 4.0.4 on 2022-05-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_category_alter_post_published_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=250),
        ),
    ]