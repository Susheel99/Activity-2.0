# Generated by Django 3.2.4 on 2021-06-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
