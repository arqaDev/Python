# Generated by Django 2.1.5 on 2019-09-15 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='image',
            new_name='image_field',
        ),
    ]
