# Generated by Django 5.0.2 on 2024-02-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agenda", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="tag",
            field=models.CharField(max_length=255, null=True),
        ),
    ]