# Generated by Django 3.2.8 on 2022-08-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20220808_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(related_name='teachers', to='school.Student'),
        ),
    ]