# Generated by Django 4.0.6 on 2022-08-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='origin_county',
            new_name='origin_country',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phoneneumber',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='customer',
            name='occupation',
            field=models.CharField(max_length=20, null=True),
        ),
    ]