# Generated by Django 4.2.4 on 2023-09-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0005_alter_usersubscription_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionitems',
            name='subscription_item_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
