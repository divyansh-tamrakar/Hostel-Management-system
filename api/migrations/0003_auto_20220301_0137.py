# Generated by Django 2.2.14 on 2022-02-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220301_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='occupiedBy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='spaceFor',
            field=models.TextField(blank=True, null=True),
        ),
    ]
