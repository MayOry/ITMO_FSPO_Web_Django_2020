# Generated by Django 3.1.2 on 2020-11-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izdat_app', '0004_remove_author_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='edition',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
