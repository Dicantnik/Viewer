# Generated by Django 4.2.6 on 2023-12-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0003_alter_room_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="uuid",
            field=models.CharField(max_length=20),
        ),
    ]