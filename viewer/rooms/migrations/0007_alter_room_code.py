# Generated by Django 4.2.6 on 2023-12-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_alter_room_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="code",
            field=models.CharField(default="Yrllk6", max_length=20),
        ),
    ]
