# Generated by Django 3.0.5 on 2021-08-11 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_club'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='chef_id',
            new_name='chef',
        ),
    ]