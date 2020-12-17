# Generated by Django 3.1.2 on 2020-12-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporte',
            old_name='video2',
            new_name='video',
        ),
        migrations.AddField(
            model_name='reporte',
            name='is_reported',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reporte',
            name='is_solved',
            field=models.BooleanField(default=False),
        ),
    ]
