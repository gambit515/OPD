# Generated by Django 4.2.20 on 2025-04-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidbook_app', '0009_studentrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrequest',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='student_requests/', verbose_name='Прикрепленный файл'),
        ),
    ]
