# Generated by Django 2.0.4 on 2018-07-08 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0003_auto_20180708_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='details',
            new_name='detail',
        ),
    ]