# Generated by Django 4.2.6 on 2023-12-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0007_alter_room_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="videocode",
            field=models.CharField(default="ERROR", max_length=20),
        ),
        migrations.AlterField(
            model_name="room",
            name="code",
            field=models.CharField(default="W3oXuX", max_length=20),
        ),
    ]