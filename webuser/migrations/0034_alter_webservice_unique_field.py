# Generated by Django 3.2.6 on 2023-03-20 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0033_alter_webservice_unique_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webservice',
            name='unique_field',
            field=models.CharField(default='4ff50329739242e7a1335e0ed40cbd5d', editable=False, max_length=32, unique=True),
        ),
    ]
