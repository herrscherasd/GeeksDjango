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