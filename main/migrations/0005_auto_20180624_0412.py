# Generated by Django 2.0.6 on 2018-06-24 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180621_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fechaInicio',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fechaTermino',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
