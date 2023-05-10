from django.db import models

# Create your models here.
class Academy(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название курса")
    content = models.TextField(verbose_name="Описание курса")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

class Courses(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')
    course_for = models.CharField(max_length=50, verbose_name='Курсы для:')
    is_laptop = models.BooleanField(verbose_name="Наличие ноутбука")
    course = models.CharField(max_length=100, verbose_name='Выбор направления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форма пользователя"
        verbose_name_plural = "Формы пользователей"
