# Generated by Django 4.1.6 on 2023-05-02 05:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cakes_carts_orders_reviews_delete_cakebox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_deliverydate',
            field=models.DateField(default=datetime.date(2023, 5, 3)),
        ),
    ]
