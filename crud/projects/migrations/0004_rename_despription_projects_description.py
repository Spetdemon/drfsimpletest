# Generated by Django 5.0.6 on 2024-05-22 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='despription',
            new_name='description',
        ),
    ]