# Generated by Django 3.1.2 on 2020-12-12 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0002_reporte_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='video2',
            field=models.FileField(blank=True, null=True, upload_to='reportes/videos/'),
        ),
    ]
