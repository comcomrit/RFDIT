# Generated by Django 3.1.1 on 2020-09-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examscore',
            name='score',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
