# Generated by Django 5.1 on 2024-09-06 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0018_remove_payment_cart_payment_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='details',
            new_name='detail',
        ),
    ]
