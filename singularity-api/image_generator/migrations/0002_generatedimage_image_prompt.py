# Generated by Django 4.2.4 on 2023-09-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedimage',
            name='image_prompt',
            field=models.CharField(default='', max_length=5000),
        ),
    ]