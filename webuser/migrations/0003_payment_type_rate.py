# Generated by Django 3.2.6 on 2023-01-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0002_payment_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_type',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
