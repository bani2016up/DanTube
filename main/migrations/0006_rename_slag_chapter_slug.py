# Generated by Django 4.0.2 on 2022-03-27 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_chapter_color_chapter_color_color_chapter_color2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='slag',
            new_name='slug',
        ),
    ]
