# Generated by Django 5.0.7 on 2024-09-21 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('current', 'current'), ('savings', 'savings')], max_length=100),
        ),
    ]
