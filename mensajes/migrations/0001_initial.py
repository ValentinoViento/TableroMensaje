# Generated by Django 4.2 on 2024-08-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textoMensaje', models.TextField()),
                ('remitente', models.CharField(max_length=15)),
                ('destinatario', models.CharField(max_length=15)),
            ],
        ),
    ]
