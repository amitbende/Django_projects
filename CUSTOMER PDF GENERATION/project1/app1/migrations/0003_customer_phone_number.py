# Generated by Django 4.0.4 on 2022-06-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_menu_customer_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.BigIntegerField(default=9856321458),
            preserve_default=False,
        ),
    ]
