# Generated by Django 4.2.3 on 2023-08-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_varianteprecio'),
    ]

    operations = [
        migrations.AddField(
            model_name='varianteprecio',
            name='codigo_barras',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
