# Generated by Django 4.2.3 on 2023-08-03 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_conversacion_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='productos/', verbose_name='Imagen o Video'),
        ),
    ]
