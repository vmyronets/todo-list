from django.urls import path

from task.views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_status,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "task"

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path("tasks/<int:pk>/toggle/", toggle_task_status, name="task-toggle"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete")
]
