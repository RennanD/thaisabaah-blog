# Generated by Django 2.1.5 on 2019-01-08 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190104_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_capa',
        ),
    ]
