from tasks.models import Task
from django.contrib import admin

admin.site.site_header = "Schedule: TASKS"
admin.site.register(Task)
