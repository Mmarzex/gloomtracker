# Generated by Django 2.1.5 on 2019-01-07 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gloomtracker_api', '0005_items_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
