# Generated by Django 4.0.3 on 2022-03-17 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_viewedby'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-pub_date']},
        ),
    ]