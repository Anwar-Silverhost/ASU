# Generated by Django 5.0 on 2023-12-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_user', '0004_alter_userregistration_db_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration_db',
            name='dateofbirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
