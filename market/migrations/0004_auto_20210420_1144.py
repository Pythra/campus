# Generated by Django 3.1.8 on 2021-04-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='typ',
            field=models.CharField(choices=[('room', 'RM'), ('hostel', 'HOS'), ('self-contain', 'CON'), ('flat', 'FLA')], max_length=20),
        ),
    ]
