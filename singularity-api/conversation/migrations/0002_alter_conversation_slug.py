# Generated by Django 4.2.4 on 2023-09-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='slug',
            field=models.UUIDField(auto_created=True, db_index=True, unique=True),
        ),
    ]
