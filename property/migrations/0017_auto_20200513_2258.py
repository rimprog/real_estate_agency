# Generated by Django 2.2.4 on 2020-05-13 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20200512_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='квартиры'),
        ),
    ]
