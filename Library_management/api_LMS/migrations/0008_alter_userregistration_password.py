# Generated by Django 5.1.5 on 2025-02-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_LMS', '0007_alter_userregistration_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
