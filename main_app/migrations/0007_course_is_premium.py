# Generated by Django 4.2.1 on 2023-10-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_prerequisites_course_prerequisites'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]