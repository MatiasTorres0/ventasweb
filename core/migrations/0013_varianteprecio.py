# Generated by Django 4.2.3 on 2023-08-04 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_tamano_unidad_medida_alter_producto_tamano_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariantePrecio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('peso_kilo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('unidad', models.CharField(blank=True, max_length=10, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]
