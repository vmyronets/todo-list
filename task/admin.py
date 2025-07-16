from django.contrib import admin

from task.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "complete_by", "completed"]
    list_filter = ["completed", "tags"]
    search_fields = ["content"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
