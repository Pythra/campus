# Generated by Django 3.1.8 on 2021-04-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20210420_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='status',
            field=models.CharField(choices=[('For rent', 'For rent'), ('Female roommate needed', 'Female roommate needed'), ('Male roommate needed', 'Male roommate needed')], default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='house',
            name='address',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='pic1',
            field=models.ImageField(upload_to='house_pics'),
        ),
        migrations.AlterField(
            model_name='house',
            name='pic2',
            field=models.ImageField(blank=True, null=True, upload_to='house_pics'),
        ),
        migrations.AlterField(
            model_name='house',
            name='pic3',
            field=models.ImageField(blank=True, null=True, upload_to='house_pics'),
        ),
        migrations.AlterField(
            model_name='house',
            name='pic4',
            field=models.ImageField(blank=True, null=True, upload_to='house_pics'),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]
