# Generated by Django 4.2.5 on 2023-09-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]