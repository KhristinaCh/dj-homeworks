# Generated by Django 3.2.8 on 2022-08-12 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'ordering': ['id']},
        ),
    ]
