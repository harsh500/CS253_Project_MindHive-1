# Generated by Django 3.2.12 on 2022-04-03 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 12, 49, 35, 378404), verbose_name='date published'),
        ),
    ]