# Generated by Django 4.2.2 on 2023-06-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingDate',
            field=models.DateField(),
        ),
    ]
