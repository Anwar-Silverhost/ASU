# Generated by Django 5.0 on 2023-12-13 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_user', '0001_initial'),
        ('admin_user', '0003_academic_db_savedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration_db',
            name='EnrolmentNo',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='userregistration_db',
            name='academic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_user.academic_db'),
        ),
    ]