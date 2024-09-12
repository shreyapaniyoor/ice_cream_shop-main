# Generated by Django 5.1 on 2024-08-16 14:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('image_url', models.ImageField(upload_to='products/images/')),
                ('brand', models.CharField(choices=[("Ben & Jerry's", "Ben & Jerry's"), ('Magnum', 'Magnum'), ('Dairy Queen', 'Dairy Queen')], default='Magnum', max_length=50)),
                ('category', models.CharField(choices=[('Ice Cream', 'Ice Cream'), ('Gelato', 'Gelato'), ('Ice Cream Bars', 'Ice Cream Bars')], default='Ice Cream', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default='vinod', on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
