# Generated by Django 4.2.7 on 2023-12-07 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaRiver', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre',
            new_name='articulo',
        ),
    ]
