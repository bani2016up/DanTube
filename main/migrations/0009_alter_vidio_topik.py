# Generated by Django 4.0.2 on 2022-03-27 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidio',
            name='topik',
            field=models.ManyToManyField(to='main.Chapter'),
        ),
    ]
