from django.urls import path

from university.views import *

urlpatterns = [
    path('teachers/', get_teachers, name='teachers'),
    path('teacher/add/', add_teacher, name='add_teacher'),
    path('teacher/<int:teacher_id>/', view_teacher, name='view_teacher'),
    path('teacher/<int:teacher_id>/edit', edit_teacher, name='edit_teacher'),
    path('teacher/<int:teacher_id>/delete', delete_teacher, name='delete_teacher'),

    path('subjects/', get_subjects, name='subjects'),
    path('subject/add', add_subject, name='add_subject'),
    path('subject/<int:subject_id>/', view_subject, name='view_subject'),
    path('subject/<int:subject_id>/edit', edit_subject, name='edit_subject'),
    path('subject/<int:subject_id>/delete', delete_subject, name='delete_subject'),
]
