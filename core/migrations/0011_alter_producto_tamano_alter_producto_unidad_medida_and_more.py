# Generated by Django 4.2.3 on 2023-08-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_producto_tamano_alter_producto_unidad_medida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tamano',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidad_medida',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Tamano',
        ),
        migrations.DeleteModel(
            name='Unidad_medida',
        ),
    ]