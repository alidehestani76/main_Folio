# Generated by Django 2.0.4 on 2018-04-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_name', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('lastname', models.TextField()),
                ('gender', models.CharField(max_length=2)),
                ('birthday', models.DateField()),
            ],
        ),
    ]