# Generated by Django 4.0.2 on 2022-03-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_slag_chapter_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vidio',
            name='topik',
        ),
        migrations.AddField(
            model_name='vidio',
            name='topik',
            field=models.ManyToManyField(null=True, to='main.Chapter'),
        ),
    ]
