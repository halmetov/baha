# Generated by Django 3.1.5 on 2021-01-13 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_blog_which_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=300)),
                ('person', models.CharField(blank=True, default='', max_length=300)),
                ('phone', models.CharField(blank=True, default='', max_length=300)),
                ('address', models.CharField(blank=True, default='', max_length=300)),
                ('payed', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('session_id', models.CharField(blank=True, default='', max_length=300)),
                ('amount', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('orig_price', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('product_price', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]
