# Generated by Django 3.2 on 2021-04-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_alter_restaurantinfo_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantinfo',
            name='main_image',
            field=models.ImageField(default='static/images/pic01.jpg', upload_to='media'),
        ),
    ]