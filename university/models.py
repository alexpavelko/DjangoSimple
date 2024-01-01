from django.db import models

from university.constants import COURSE_CHOICES, GRADE_CHOICES, JOB_POSITION_CHOICES


class Group(models.Model):
    title = models.CharField(max_length=10, verbose_name="Группа")
    course = models.IntegerField(choices=COURSE_CHOICES, verbose_name="Курс обучения")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f'{self.title}, {self.course} курс'


class Student(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    ticket_number = models.CharField(max_length=15, verbose_name="№ студенческого билета")
    email = models.EmailField(max_length=30, verbose_name="Email студента")
    group = models.ForeignKey(to=Group, related_name="students", on_delete=models.CASCADE, verbose_name="Группа")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    email = models.EmailField(max_length=30, verbose_name="Email преподавателя")
    job_position = models.CharField(max_length=40, choices=JOB_POSITION_CHOICES, verbose_name="Должность")

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return f'{self.first_name} {self.last_name}, должность: {self.job_position}'


class Subject(models.Model):
    title = models.CharField(max_length=80, verbose_name="Название предмета")
    group = models.ForeignKey(to=Group, related_name="subjects", on_delete=models.CASCADE, verbose_name="Группа")
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE,
                                verbose_name="Преподаватель, который ведет предмет")


class Grade(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, verbose_name="Студент")
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    grade = models.PositiveIntegerField(choices=GRADE_CHOICES)
    graduating_date = models.DateField(verbose_name="Дата выставления оценки")
