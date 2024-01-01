from django import forms
from .models import *


class TeacherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['creation_date', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'email': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'job_position': forms.Select(attrs={'class': 'form-select', 'style': 'width: 400px;'}, choices=Teacher.JOB_POSITION_CHOICES),
        }


class SubjectForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 600px;'}),
            'teacher': forms.Select(attrs={'class': 'form-select', 'style': 'width: 600px;'}, choices=Teacher.JOB_POSITION_CHOICES),
        }
