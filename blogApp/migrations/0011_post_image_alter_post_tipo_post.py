# Generated by Django 4.0.4 on 2022-06-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0010_alter_panels_panel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='tipo_post',
            field=models.CharField(choices=[('Monocrystalline', 'Pelicula'), ('Polycrystalline', 'Libro')], max_length=40),
        ),
    ]
