# Generated by Django 3.1.2 on 2021-01-02 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='which_one',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='main.blogcategory'),
        ),
    ]