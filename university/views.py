from django.shortcuts import render, redirect

from university.forms import *
from university.models import *


# region teacher


def get_teachers(request):
    teachers = Teacher.objects.all().order_by('-job_position')

    context = {
        'teachers': teachers,
    }

    return render(request, "teacher/view_teachers.html", context)


def add_teacher(request):
    teacher_form = TeacherForm()
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
    if teacher_form.is_valid():
        teacher = teacher_form.save()

        teacher.save()
        return redirect(f'/teacher/{teacher.id}')
    context = {
        'title': 'Добавить учителя',
        'confirm_button': 'Добавить',
        'form': teacher_form,
    }

    return render(request, "form.html", context)


def view_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    teacher_subjects = Subject.objects.filter(teacher=teacher)
    context = {
        'teacher': teacher,
        'teacher_subjects': teacher_subjects,
        'teacher_fields': Teacher._meta.fields
    }
    return render(request, "teacher/view_teacher.html", context)


def edit_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    teacher_form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            teacher.first_name = teacher_form.cleaned_data['first_name']
            teacher.last_name = teacher_form.cleaned_data['last_name']
            teacher.email = teacher_form.cleaned_data['email']
            teacher.job_position = teacher_form.cleaned_data['job_position']
            teacher.save()
            return redirect(f'/teacher/{teacher_id}')
    context = {
        'title': 'Редактировать учителя',
        'confirm_button': 'Редактировать',
        'form': teacher_form,
    }
    return render(request, "form.html", context)


def delete_teacher(request, teacher_id):
    Teacher.objects.get(id=teacher_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))

# endregion


# region subject


def get_subjects(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
    }

    return render(request, "subject/view_subjects.html", context)


def add_subject(request):
    subject_form = SubjectForm()
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
    if subject_form.is_valid():
        subject = subject_form.save()
        subject.save()
        return redirect(f'/subject/{subject.id}')
    context = {
        'title': 'Добавить предмет',
        'confirm_button': 'Добавить',
        'form': subject_form,
    }

    return render(request, "form.html", context)


def view_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)

    context = {
        'subject': subject,
    }
    return render(request, "subject/view_subject.html", context)


def edit_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject_form = SubjectForm(instance=subject)

    if request.method == 'POST':
        subject_form = SubjectForm(request.POST, instance=subject)
        if subject_form.is_valid():
            subject = subject_form.save(commit=False)
            subject.title = subject_form.cleaned_data['title']
            subject.teacher = subject_form.cleaned_data['teacher']
            subject.group = subject_form.cleaned_data['group']
            subject.save()
            return redirect(f'/subject/{subject_id}')

    context = {
        'title': 'Редактировать предмет',
        'confirm_button': 'Редактировать',
        'form': subject_form,
    }
    return render(request, "form.html", context)


def delete_subject(request, subject_id):
    Subject.objects.get(id=subject_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


# endregion


# region group


def get_groups(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }

    return render(request, "group/view_groups.html", context)


def add_group(request):
    group_form = GroupForm()
    if request.method == 'POST':
        group_form = GroupForm(request.POST)
    if group_form.is_valid():
        group = group_form.save()
        group.save()
        return redirect(f'/group/{group.id}')
    context = {
        'title': 'Добавить группу',
        'confirm_button': 'Добавить',
        'form': group_form,
    }

    return render(request, "form.html", context)


def view_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group_students = Student.objects.filter(group=group)
    context = {
        'group': group,
        'group_students': group_students,
    }
    return render(request, "group/view_group.html", context)


def edit_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group_form = GroupForm(instance=group)
    if request.method == 'POST':
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group.title = group_form.cleaned_data['title']
            group.course = group_form.cleaned_data['course']
            group.save()
            return redirect(f'/group/{group_id}')
    context = {
        'title': 'Редактировать группу',
        'confirm_button': 'Редактировать',
        'form': group_form,
    }
    return render(request, "form.html", context)


def delete_group(request, group_id):
    Group.objects.get(id=group_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


# endregion

