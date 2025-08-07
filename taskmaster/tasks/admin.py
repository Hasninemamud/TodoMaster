from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'priority', 'completed', 'created_at')
    list_filter = ('completed', 'priority', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)