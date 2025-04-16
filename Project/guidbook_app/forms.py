from django import forms
from .models import StudentRequest

class StudentRequestForm(forms.ModelForm):
    class Meta:
        model = StudentRequest
        fields = ['faculty', 'course', 'subject', 'work_type', 'student_name', 'contact_info', 'file']
        widgets = {
            'faculty': forms.TextInput(attrs={'placeholder': 'Введите факультет'}),
            'course': forms.TextInput(attrs={'placeholder': 'Введите курс'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Введите предмет'}),
            'work_type': forms.TextInput(attrs={'placeholder': 'Введите тип работы'}),
            'student_name': forms.TextInput(attrs={'placeholder': 'Введите ФИО'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Введите контактные данные'}),
        }
        labels = {
            'faculty': 'Факультет',
            'course': 'Курс',
            'subject': 'Предмет',
            'work_type': 'Тип работы(пока что только лекция)',
            'student_name': 'ФИО',
            'contact_info': 'Контактные данные для связи',
            'file': 'Файл с работой',
        }