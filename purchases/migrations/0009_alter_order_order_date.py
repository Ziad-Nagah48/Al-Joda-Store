# Generated by Django 4.2.1 on 2023-05-16 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0008_alter_order_order_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 16, 15, 40, 32, 227581, tzinfo=datetime.timezone.utc)),
        ),
    ]
