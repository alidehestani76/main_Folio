# Generated by Django 2.0.4 on 2018-04-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('volume', models.DecimalField(decimal_places=8, max_digits=10)),
                ('value', models.DecimalField(decimal_places=8, max_digits=10)),
                ('count_Of_Transaction', models.DecimalField(decimal_places=8, max_digits=10)),
                ('max_V', models.DecimalField(decimal_places=8, max_digits=10)),
                ('min_V', models.DecimalField(decimal_places=8, max_digits=10)),
                ('final_Amount', models.DecimalField(decimal_places=8, max_digits=10)),
                ('final_Change', models.DecimalField(decimal_places=8, max_digits=10)),
                ('final_Persentage', models.FloatField()),
                ('lastest_Amount', models.DecimalField(decimal_places=8, max_digits=10)),
                ('lastest_Change', models.DecimalField(decimal_places=8, max_digits=10)),
                ('lastest_Percentage', models.FloatField()),
                ('yesterday', models.DecimalField(decimal_places=8, max_digits=10)),
                ('index_Percentage', models.FloatField()),
                ('PE', models.DecimalField(decimal_places=8, max_digits=10)),
                ('EPS', models.DecimalField(decimal_places=8, max_digits=10)),
                ('stock_Market_Value', models.DecimalField(decimal_places=8, max_digits=10)),
                ('best_Supply', models.DecimalField(decimal_places=8, max_digits=10)),
                ('best_Demand', models.DecimalField(decimal_places=8, max_digits=10)),
                ('market', models.TextField()),
            ],
        ),
    ]
