# Generated by Django 4.2.4 on 2024-04-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
