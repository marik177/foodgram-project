# Generated by Django 3.2.15 on 2022-08-09 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20220809_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientamount',
            old_name='name',
            new_name='ingredient',
        ),
    ]
