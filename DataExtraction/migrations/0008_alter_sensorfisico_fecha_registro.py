# Generated by Django 5.1.2 on 2024-10-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataExtraction', '0007_alter_sensorfisico_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorfisico',
            name='fecha_registro',
            field=models.DateTimeField(),
        ),
    ]
