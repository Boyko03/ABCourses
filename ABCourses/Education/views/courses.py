from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from Education.models import Course


def list(request):
    return render(request, 'courses/list.html',
                  {'courses': Course.objects.all()})


def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/detail.html', {'course': course})


def edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/edit.html', {'course': course})


class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'level', 'description']
    template_name = 'courses/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('Education:courses:detail',
                            kwargs={'course_id': self.object.id})


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name', 'level', 'description']
    template_name = 'courses/edit.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('Education:courses:detail',
                            kwargs={'course_id': self.object.id})
