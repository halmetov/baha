# Generated by Django 3.1.2 on 2020-12-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_blogcomment_blog_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcomment',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]
