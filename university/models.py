from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=10, verbose_name="Группа")
    COURSE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    course = models.IntegerField(choices=COURSE_CHOICES, verbose_name="Курс обучения")


class Student(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    ticket_number = models.CharField(max_length=15, verbose_name="№ студенческого билета")
    email = models.EmailField(max_length=30, unique=True, verbose_name="Email студента")
    COURSE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    group = models.ForeignKey(to=Group, related_name="students", on_delete=models.CASCADE, verbose_name="Группа")


class Teacher(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    email = models.EmailField(max_length=30, unique=True, verbose_name="Email студента")
    JOB_POSITION_CHOICES = [
        ("Ассистент", "Ассистент"),
        ("Старший преподователь", "Старший преподователь"),
        ("Доцент", "Доцент"),
        ("Профессор", "Профессор"),
    ]
    job_position = models.CharField(choices=JOB_POSITION_CHOICES, verbose_name="Должность")


class Subject(models.Model):
    title = models.CharField(max_length=10, verbose_name="Название предмета")
    COURSE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    teacher = models.ForeignKey(to=Teacher, related_name="subjects", on_delete=models.CASCADE, verbose_name="Преподователь, который ведет предмет")


class Grade(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, verbose_name="Студент")
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    CHOICES_GRADE = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    grade = models.PositiveIntegerField(choices=CHOICES_GRADE)
    graduating_date = models.DateField(verbose_name="Дата выставления оценки")
