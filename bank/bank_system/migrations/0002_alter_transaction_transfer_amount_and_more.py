# Generated by Django 4.1.1 on 2022-10-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transfer_amount',
            field=models.FloatField(default=0.0, max_length=5),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.FloatField(default=0.0, editable=False, max_length=5),
        ),
    ]