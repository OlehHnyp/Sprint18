# Generated by Django 3.1.1 on 2021-03-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_auto_20210327_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
