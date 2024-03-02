from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.redirect_to_current_month, name="redirect_to_current_month"),
    path("<int:year>/<str:month>/", views.agenda, name="agenda"),
    path("reminder/", views.reminder, name="reminder"),
    path("schedule/", views.schedule_event, name="schedule_event"),
    path("edit/<int:event_id>/", views.edit_event, name="edit_event"),
    path("delete/<int:event_id>/", views.delete_event, name="delete_event"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
