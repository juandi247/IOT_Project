# Generated by Django 5.1.2 on 2024-10-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataExtraction', '0005_alter_sensordata_enqueued_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorfisico',
            name='fecha_registro',
            field=models.DateTimeField(),
        ),
    ]