# Generated by Django 4.0.4 on 2022-06-16 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogApp', '0007_alter_comentarios_creado_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
