from django.urls import path

from university.views import *

urlpatterns = [
    path('teachers/', get_teachers, name='get_teachers'),
    path('teacher/add/', add_teacher, name='add_teacher'),
    path('teacher/<int:teacher_id>/', view_teacher, name='view_teacher'),
    path('teacher/<int:teacher_id>/edit', edit_teacher, name='edit_teacher'),
    path('teacher/<int:teacher_id>/delete', delete_teacher, name='delete_teacher'),

    path('subjects/', get_subjects, name='get_subjects'),
    path('subject/add', add_subject, name='add_subject'),
    path('subject/<int:subject_id>/', view_subject, name='view_subject'),
    path('subject/<int:subject_id>/edit', edit_subject, name='edit_subject'),
    path('subject/<int:subject_id>/delete', delete_subject, name='delete_subject'),

    path('groups/', get_groups, name='add_groups'),
    path('group/add', add_group, name='add_group'),
    path('group/<int:group_id>/', view_group, name='view_group'),
    path('group/<int:group_id>/edit', edit_group, name='edit_group'),
    path('group/<int:group_id>/delete', delete_group, name='delete_group'),

    path('students/', get_students, name='get_students'),
    path('student/add', add_student, name='add_student'),
    path('student/<int:student_id>/', view_student, name='view_student'),
    path('student/<int:student_id>/edit', edit_student, name='edit_student'),
    path('student/<int:student_id>/delete', delete_student, name='delete_student'),

    path('grade/<int:student_id>/add', add_student_grade, name='add_student_grade'),
    path('grade/<int:grade_id>/edit', edit_student_grade, name='edit_student_grade'),
    path('grade/<int:grade_id>/delete', delete_student_grade, name='delete_student_grade'),

]
