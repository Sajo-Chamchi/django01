# Generated by Django 4.0.6 on 2022-09-01 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='topics',
            new_name='topic',
        ),
    ]