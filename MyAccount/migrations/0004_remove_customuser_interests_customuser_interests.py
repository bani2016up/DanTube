# Generated by Django 4.0.2 on 2022-03-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_vidio_topik'),
        ('MyAccount', '0003_customuser_date_of_birth_customuser_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='interests',
        ),
        migrations.AddField(
            model_name='customuser',
            name='interests',
            field=models.ManyToManyField(null=True, to='main.Chapter'),
        ),
    ]
