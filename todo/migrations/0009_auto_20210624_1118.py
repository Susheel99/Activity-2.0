# Generated by Django 2.2.7 on 2021-06-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_merge_20210624_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]