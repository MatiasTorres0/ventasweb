# Generated by Django 4.2.3 on 2023-07-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_producto_stock_alter_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo_barras',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
