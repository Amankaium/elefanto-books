# Generated by Django 5.0 on 2023-12-06 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_book_publicated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publicated_at',
            new_name='publicated_date',
        ),
    ]