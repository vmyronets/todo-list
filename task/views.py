from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from task.models import Task, Tag


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-created")
    return render(
        request,
        template_name="task/index.html",
        context={"tasks": tasks}
    )


class TaskListView(generic.ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-created")


