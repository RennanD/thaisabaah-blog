# Generated by Django 2.1.4 on 2018-12-27 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='new_field',
            field=models.TextField(default='SOME STRING'),
        ),
    ]