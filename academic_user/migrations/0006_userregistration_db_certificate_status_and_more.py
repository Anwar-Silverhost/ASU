# Generated by Django 5.0 on 2023-12-14 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_user', '0005_alter_userregistration_db_dateofbirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration_db',
            name='Certificate_status',
            field=models.CharField(default='Not Issued', max_length=240),
        ),
        migrations.AddField(
            model_name='userregistration_db',
            name='user_status',
            field=models.CharField(default='Not Completed', max_length=240),
        ),
    ]
