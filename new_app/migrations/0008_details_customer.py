# Generated by Django 5.1 on 2024-09-05 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0007_payment_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='new_app.customer'),
            preserve_default=False,
        ),
    ]
