# Generated by Django 4.1.2 on 2023-06-17 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_application_fees"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Application_Fees",
        ),
    ]