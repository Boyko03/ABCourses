from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django import forms

from Education.models import BaseUser


def is_logged(func):
    def inner(request, *args, **kwargs):
        if request.session.get('user_id'):
            return redirect(reverse('Education:courses:list'))
        else:
            return func(request, *args, **kwargs)
    return inner


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = BaseUser
        fields = ['name', 'email', 'password', 'role']


@is_logged
def create_user(request):
    if request.method == "POST":
        data = request.POST
        form = UserForm(data=data)
        if form.is_valid():
            user = form.save()
            if user.role == 'teacher':
                request.session['role'] = 'teacher'
            else:
                request.session['role'] = 'student'
            request.session['user_id'] = user.user_id
            request.session['user_name'] = user.name
            request.session['user_email'] = user.email
            return redirect(reverse('Education:courses:list'))
        else:
            return render(request, 'login/registration.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'login/registration.html', {'form': form})


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = BaseUser
        fields = ['email', 'password']


@is_logged
def log_user(request):
    if request.method == "POST":
        data = request.POST
        form = LoginForm(data=data)
        request.session['here'] = 0
        if form.is_valid():
            request.session['here'] = 1
            user = BaseUser.objects.get(email=form.email)
            request.session['here'] = 2
            if user:
                request.session['here'] = 3
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.name
                request.session['user_email'] = user.email
                return redirect(reverse('Education:courses:list'))
            else:
                request.session['here'] = 4
                return render(request, 'login/login.html', {'form': form})
        else:
            request.session['here'] = 5
            return render(request, 'login/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})
