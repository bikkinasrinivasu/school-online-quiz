# Generated by Django 2.2.7 on 2021-07-27 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210728_0241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userquizanswers',
            old_name='correct_correct',
            new_name='correct_answer',
        ),
    ]
