# Generated by Django 4.2.4 on 2023-09-08 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('llama', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialogmessage',
            name='conversation',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='DialogMessage',
        ),
    ]
