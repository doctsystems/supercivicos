# Generated by Django 3.1.2 on 2020-10-19 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_auto_20201019_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
