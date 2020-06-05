from django.urls import path, include

from Education.views import index, courses, login

app_name = 'Education'


courses_patterns = [
    path('', courses.list, name='list'),
    path('<int:course_id>/', courses.detail, name='detail'),
    path('new/', courses.CourseCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', courses.CourseUpdateView.as_view(), name='edit'),
    path('delete/<int:course_id>/', courses.delete_course, name='delete'),
    path('<int:course_id>/new/', courses.LectureCreateView.as_view(), name='create_lecture'),
    path('<int:course_id>/<int:lecture_id>/', courses.lecture_detail, name='lecture_detail'),
    path('<int:course_id>/<int:pk>/edit/', courses.LectureUpdateView.as_view(), name='edit_lecture'),
]

urlpatterns = [
    path('', index, name='index'),
    path('courses/', include((courses_patterns, 'courses'))),
    path('login/', login.log_user, name='login'),
    path('register/', login.create_user, name='register')
]
