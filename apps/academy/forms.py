from django import forms

from apps.academy.models import Courses

class CourseFeedBackForm(forms.Form):
    your_name = forms.CharField(max_length=100, label='Ваше имя:')
    phone_number = forms.CharField(max_length=50, label='Ваш номер телефона')
    course_for = forms.CharField(max_length=50, label="Вы ищете курс для себя?")
    laptop = forms.BooleanField(label='Есть ли у вас ноутбук?')
    # course = forms.ModelChoiceField(queryset=Courses.objects.all(), label="Какое направление вас интересует?")
