# Generated by Django 4.2.4 on 2023-09-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0006_subscriptionitems_subscription_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionitems',
            name='price',
            field=models.DecimalField(decimal_places=5, default=0.009, max_digits=8),
        ),
    ]