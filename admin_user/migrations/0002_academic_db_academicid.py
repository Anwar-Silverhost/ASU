# Generated by Django 5.0 on 2023-12-11 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic_db',
            name='academicId',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
