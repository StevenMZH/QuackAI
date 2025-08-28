from django.urls import path
from .views import ScheduleTaskView

urlpatterns = [
    path("schedule/", ScheduleTaskView.as_view(), name="schedule_tasks"),
]
