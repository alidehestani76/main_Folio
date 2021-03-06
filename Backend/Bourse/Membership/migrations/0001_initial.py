# Generated by Django 2.0.4 on 2018-05-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bourseapp', '0004_auto_20180423_1432'),
        ('Personapp', '0005_auto_20180531_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_stocks_person_has', models.IntegerField(default=0)),
                ('bourse', models.ForeignKey(on_delete=True, related_name='fk_bourse', to='Bourseapp.Bourse')),
                ('person', models.ForeignKey(on_delete=True, related_name='fk_person', to='Personapp.Person')),
            ],
        ),
    ]
