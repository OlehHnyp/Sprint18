# Generated by Django 3.1.1 on 2021-03-27 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210327_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='book_id',
            new_name='book',
        ),
    ]
