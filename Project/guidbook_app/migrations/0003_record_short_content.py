# Generated by Django 4.2.20 on 2025-03-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidbook_app', '0002_category_color_class_category_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='short_content',
            field=models.TextField(default='meme', verbose_name='Краткое содержание записи записи (HTML)'),
            preserve_default=False,
        ),
    ]
