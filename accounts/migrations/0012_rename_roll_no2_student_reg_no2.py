# Generated by Django 4.2 on 2023-05-17 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_rename_roll_no_student_reg_no"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="roll_no2",
            new_name="reg_no2",
        ),
    ]
