# Generated by Django 3.1.2 on 2020-12-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_productcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='blog_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
