# Generated by Django 4.0.2 on 2022-02-18 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='reationship',
            new_name='relationship',
        ),
    ]
