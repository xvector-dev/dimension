# Generated by Django 4.2.4 on 2023-09-10 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import image_generator.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=500)),
                ('image_type', models.CharField(max_length=10)),
                ('image_size', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=image_generator.models.generate_filename)),
                ('public', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated_images', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
