# Generated by Django 3.1.2 on 2020-12-16 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stickers', '0002_auto_20201215_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='stickers',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='stickers',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stickers',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='stickers',
            name='usuario_creacion',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stickers',
            name='usuario_modificacion',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]