# Generated by Django 3.2 on 2021-04-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_restaurantreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantreview',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
