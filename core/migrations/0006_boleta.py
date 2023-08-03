# Generated by Django 4.2.3 on 2023-08-02 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_producto_codigo_barras'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_boleta', models.CharField(max_length=20, unique=True)),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True)),
                ('total_a_pagar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('archivo_pdf', models.FileField(upload_to='boletas/')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]