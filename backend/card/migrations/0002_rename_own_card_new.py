# Generated by Django 3.2.6 on 2021-08-14 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='own',
            new_name='new',
        ),
    ]