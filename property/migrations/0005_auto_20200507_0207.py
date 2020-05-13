# Generated by Django 2.2.4 on 2020-05-06 23:07

from django.db import migrations


def is_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20200503_1108'),
    ]

    operations = [
        migrations.RunPython(is_new_building)
    ]
