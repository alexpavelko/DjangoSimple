from django.urls import path

from university.views import *

urlpatterns = [
    path('teachers/', get_teachers, name='teachers'),
    path('teacher/add/', add_teacher, name='add_teacher'),
    path('teacher/<int:teacher_id>/', view_teacher, name='view_teacher'),
    path('teacher/<int:teacher_id>/edit', edit_teacher, name='edit_teacher'),
    path('teacher/<int:teacher_id>/delete', delete_teacher, name='delete_teacher'),
]
