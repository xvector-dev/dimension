# Generated by Django 4.2.4 on 2023-09-09 09:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0003_remove_conversation_slug_conversation_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialogmessage',
            name='key',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
