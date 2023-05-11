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

class SettingsModel(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions =models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo",
        verbose_name="Логотип сайта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Тел.номер"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook"
    )
    instagram = models.URLField(
        verbose_name="Ссылка на Instagram"
    )
    youtube = models.URLField(
        verbose_name="Ссылка на Youtube"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройка"
        
class AboutModel(models.Model):
    image = models.ImageField(
        upload_to="about_image",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    decriptions = models.TextField(
        verbose_name="Описание"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class SlideModel(models.Model):
    image = models.ImageField(
        upload_to="slide_image",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Слайды"
        verbose_name_plural = "Слайд"

class CourseModel(models.Model):
    image = models.ImageField(
        upload_to="blog_image",
            verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"