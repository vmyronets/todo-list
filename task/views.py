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


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("task:index")
    template_name = "task/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("task:index")
    template_name = "task/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:index")
    template_name = "task/task_confirm_delete.html"


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("task:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "task/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("task:tags-list")
    template_name = "task/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("task:tags-list")
    template_name = "task/tag_form.html"
