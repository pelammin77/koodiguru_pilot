# Generated by Django 4.2.1 on 2023-11-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_tasktest'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseLogo',
            field=models.ImageField(default='course_logos/no_logo.png', upload_to='course_logos/'),
        ),
    ]