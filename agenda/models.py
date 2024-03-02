"""
Defines models for managing calendar events and reminders.

Models:
- Event: Represents an event with a title, date, time, location, description, and category.
- Reminder: Represents a reminder associated with an event, containing a reminder date and message.
"""

from django.db import models


class Event(models.Model):
    CATEGORY_CHOICES = [
        ("appointment", "Appointment"),
        ("work", "Work"),
        ("school", "School"),
        ("personal_life", "Personal Life"),
    ]

    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField(null=True)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="personal_life"
    )

    def __str__(self):
        return self.title


class Reminder(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reminder_date = models.DateField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.message
