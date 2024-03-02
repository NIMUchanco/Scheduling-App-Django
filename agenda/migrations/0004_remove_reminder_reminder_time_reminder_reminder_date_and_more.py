# Generated by Django 5.0.2 on 2024-02-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agenda", "0003_rename_tag_event_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reminder",
            name="reminder_time",
        ),
        migrations.AddField(
            model_name="reminder",
            name="reminder_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.CharField(
                choices=[
                    ("appointment", "Appointment"),
                    ("work", "Work"),
                    ("school", "School"),
                    ("personal_life", "Personal Life"),
                ],
                default="personal_life",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="reminder",
            name="message",
            field=models.TextField(null=True),
        ),
    ]