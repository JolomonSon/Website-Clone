# Generated by Django 3.1.7 on 2021-05-12 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210512_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 12, 17, 11, 51, 938323), verbose_name='date published'),
        ),
    ]
