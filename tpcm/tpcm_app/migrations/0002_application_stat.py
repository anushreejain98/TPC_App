# Generated by Django 2.1.3 on 2018-12-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpcm_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='stat',
            field=models.IntegerField(default=0),
        ),
    ]
