# Generated by Django 5.2 on 2025-04-03 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
