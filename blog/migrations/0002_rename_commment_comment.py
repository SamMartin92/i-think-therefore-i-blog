# Generated by Django 3.2.13 on 2022-06-02 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commment',
            new_name='Comment',
        ),
    ]
