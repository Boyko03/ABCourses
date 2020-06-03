from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from Education.models import Course, Lecture


def list(request):
    return render(request, 'courses/list.html',
                  {'courses': Course.objects.all()})


def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lectures = Lecture.objects.all().filter(course_id=course_id)
    return render(request, 'courses/detail.html', {'course': course, 'lectures': lectures})


def edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/edit.html', {'course': course})


def delete_course(request, course_id):
    if request.method == 'POST':
        Course.objects.get(id=course_id).delete()
    return redirect(reverse('Education:courses:list'))


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


class LectureCreateView(CreateView):
    model = Lecture
    fields = ['name', 'description', 'course']
    template_name = 'courses/create_lecture.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('Education:courses:detail',
                            kwargs={'lecture.id': self.object.id})
