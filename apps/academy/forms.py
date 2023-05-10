from django import forms

from apps.academy.models import Courses

course_types = (
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('fullstack', 'Fullstack'),
    ('android', 'Android'),
    ('iOS', 'iOS'),
    ('UX/Ui design', 'UX/UI-дизайн'),
    ('OP', 'Основы программирования'),
    ('Project_manager', 'Менеджер проектов'),
    ('None', 'Я еще не определился')
)
yes_no=(
    ('yes', 'Да'),
    ('no', "Нет")
)
class CourseFeedBackForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Ваше имя:')
    phone_number = forms.CharField(max_length=50, label='Ваш номер телефона')
    course_for = forms.CharField(max_length=50, label="Вы ищете курс для себя?")
    course = forms.ChoiceField(label="Какое направление вас интересует?", choices=course_types)

    class Meta:
        model = Courses
        fields = '__all__'