# Generated by Django 4.2.3 on 2023-08-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_varianteprecio_codigo_barras'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('Open', 'Abierto'), ('In Progress', 'En Progreso'), ('Closed', 'Cerrado')], default='Open', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
