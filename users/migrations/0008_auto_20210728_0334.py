# Generated by Django 2.2.7 on 2021-07-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210728_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='percentage',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
