"""
Functions for managing calendar events and reminders in a Django application.

Functions:
- redirect_to_current_month: Redirects to the current month's calendar view.
- agenda: Renders the calendar view for a specific year and month.
- reminder: Renders the reminder view with filtering and search functionality.
- schedule_event: Handles the creation of new events and reminders.
- edit_event: Handles the editing of existing events and reminders.
- delete_event: Handles the deletion of events.
"""

import calendar
from calendar import HTMLCalendar
from datetime import datetime, date
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Event, Reminder


def redirect_to_current_month(request):
    """
    Redirects to the current month's calendar view.

    returns:
    - A redirect to the current month's calendar view.
    """
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime("%B").lower()
    return redirect(reverse("agenda", args=[current_year, current_month]))


def agenda(request, year, month):
    """
    Renders the calendar view for a specific year and month.

    Args:
    - year: The year to display.
    - month: The month to display.

    Returns:
    - A rendered HTML page with the calendar view for the specified year and month.
    """
    events = Event.objects.all()
    month = month.capitalize()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)

    prev_month = month_num - 1 if month_num > 1 else 12
    prev_year = year if prev_month != 12 else year - 1
    next_month = month_num + 1 if month_num < 12 else 1
    next_year = year if next_month != 1 else year + 1

    prev_month = calendar.month_name[prev_month].capitalize()
    next_month = calendar.month_name[next_month].capitalize()

    cal = HTMLCalendar().formatmonth(year, month_num)

    context = {
        "events": events,
        "year": year,
        "month": month,
        "month_num": month_num,
        "cal": cal,
        "prev_month": prev_month,
        "prev_year": prev_year,
        "next_month": next_month,
        "next_year": next_year,
    }

    return render(request, "agenda/calendar.html", context)


def reminder(request):
    """
    Renders the reminder view with filtering and search functionality.

    Returns:
    - A rendered HTML page with the reminder view and search functionality.
    """
    reminders = Reminder.objects.filter(reminder_date__gt=date.today()).order_by(
        "reminder_date"
    )
    search = ""
    category = ""
    results = []

    if request.method == "POST":
        search = request.POST.get("search", "")
        category = request.POST.get("category", "")
        results = Event.objects.filter(title__icontains=search)

        if category:
            results = results.filter(category=category)

    context = {
        "reminders": reminders,
        "search": search,
        "results": results,
        "category": category,
    }

    return render(request, "agenda/reminder.html", context)


def schedule_event(request):
    """
    Handles the creation of new events and reminders.

    Returns:
    - A redirect to the current month's calendar view if the request method is POST.
    """
    if request.method == "POST":
        new_event = Event(
            title=request.POST.get("title", ""),
            date=request.POST.get("date", ""),
            time=request.POST.get("time", ""),
            location=request.POST.get("location", ""),
            description=request.POST.get("description", ""),
            category=request.POST.get("category", ""),
        )
        new_event.save()

        reminder_date_str = request.POST.get("reminder_date", "")
        message = request.POST.get("message", "")

        if reminder_date_str and message:
            reminder_date = datetime.strptime(reminder_date_str, "%Y-%m-%d").date()
            new_reminder = Reminder(
                event=new_event,
                reminder_date=reminder_date,
                message=message,
            )
            new_reminder.save()

            return redirect_to_current_month(request)

    return render(request, "agenda/schedule_form.html")


def edit_event(request, event_id):
    """
    Handles the editing of existing events and reminders.

    Args:
    - event_id: The ID of the event to edit.

    Returns:
    - A redirect to the current month's calendar view if the request method is POST.
    """
    event = get_object_or_404(Event, pk=event_id)
    reminder = Reminder.objects.filter(event=event).first()

    if request.method == "POST":
        event.title = request.POST.get("title", event.title)
        event.date = request.POST.get("date", event.date)
        event.time = request.POST.get("time", event.time)
        event.location = request.POST.get("location", event.location)
        event.description = request.POST.get("description", event.description)
        event.category = request.POST.get("category", event.category)

        reminder_date_str = request.POST.get("reminder_date", "")
        message = request.POST.get("message", "")

        if reminder_date_str and message:
            reminder_date = datetime.strptime(reminder_date_str, "%Y-%m-%d").date()
            if not reminder:
                reminder = Reminder(
                    event=event, reminder_date=reminder_date, message=message
                )
            else:
                reminder.reminder_date = reminder_date
                reminder.message = message
            reminder.save()

        event.save()
        return redirect_to_current_month(request)

    context = {
        "event": event,
        "reminder": reminder,
    }

    return render(request, "agenda/edit_form.html", context)


def delete_event(request, event_id):
    """
    Handles the deletion of events.

    Args:
    - event_id: The ID of the event to delete.

    Returns:
    - A redirect to the current month's calendar view if the request method is POST.
    """
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        event.delete()
    return redirect_to_current_month(request)
