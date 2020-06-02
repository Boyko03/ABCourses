from django.urls import path, include

from Education.views import index, courses

app_name = 'Education'


courses_patterns = [
    path('', courses.list, name='list'),
    path('<int:course_id>/', courses.detail, name='detail'),
    path('new/', courses.CourseCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', courses.CourseUpdateView.as_view(), name='edit'),
]

urlpatterns = [
    path('', index, name='index'),
    path('courses/', include((courses_patterns, 'courses')))
]
