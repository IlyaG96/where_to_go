# Generated by Django 4.0.1 on 2022-02-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_image_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='latitude',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='point',
            name='longitude',
            field=models.FloatField(verbose_name='Долгота'),
        ),
    ]
