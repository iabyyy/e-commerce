# Generated by Django 5.1 on 2024-09-06 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0021_remove_payment_status_details_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='new_app.cartitem'),
            preserve_default=False,
        ),
    ]
