# Generated by Django 4.2.1 on 2023-05-29 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_app', '0003_alter_dish_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='image',
        ),
    ]
