from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from Education.models import Course, Lecture


def login_required(func):
    def inner(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect(reverse('Education:login'))
        else:
            return func(request, *args, **kwargs)
    return inner


@login_required
def list(request):
    return render(request, 'courses/list.html',
                  {'courses': Course.objects.all()})


@login_required
def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lectures = Lecture.objects.all().filter(course_id=course_id)
    return render(request, 'courses/detail.html', {'course': course, 'lectures': lectures})


@login_required
def edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/edit.html', {'course': course})


@login_required
def delete_course(request, course_id):
    if request.method == 'POST':
        Course.objects.get(id=course_id).delete()
    return redirect(reverse('Education:courses:list'))


def lecture_detail(request, course_id, lecture_id):
    course = get_object_or_404(Course, id=course_id)
    lecture = Lecture.objects.get(id=lecture_id)
    return render(request, 'courses/lecture_detail.html', {'course': course, 'lecture': lecture})


def edit_lecture(request, course_id, lecture_id):
    course = get_object_or_404(Course, id=course_id)
    lecture = Lecture.objects.get(id=lecture_id)
    return render(request, 'course/edit_lecture.html', {'course': course, 'lecture': lecture})


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
    fields = ['name', 'description', 'course', 'url']
    template_name = 'courses/create_lecture.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('Education:courses:lecture_detail',
                            kwargs={'course_id': self.object.course.id, 'lecture_id': self.object.id})


class LectureUpdateView(UpdateView):
    model = Lecture
    fields = ['name', 'description', 'course', 'url']
    template_name = 'courses/edit_lecture.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('Education:courses:lecture_detail',
                            kwargs={'course_id': self.object.course.id, 'lecture_id': self.object.id})
