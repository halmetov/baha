# Generated by Django 3.1.2 on 2020-12-23 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_blog_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_qoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('action', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.blog')),
            ],
        ),
    ]
