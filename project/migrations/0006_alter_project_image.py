# Generated by Django 3.2.4 on 2021-06-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='photos/project/ben-4wxWBy8Jo1I-unsplash.jpg', upload_to='photos/project'),
        ),
    ]
