# Generated by Django 2.0.4 on 2018-07-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('length', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
                ('size', models.TextField(null=True)),
                ('link', models.TextField()),
            ],
        ),
    ]
