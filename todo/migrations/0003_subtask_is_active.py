# Generated by Django 3.2.4 on 2021-06-16 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210615_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]