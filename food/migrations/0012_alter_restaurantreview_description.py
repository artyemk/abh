# Generated by Django 3.2 on 2021-04-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_alter_restaurantreview_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantreview',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
