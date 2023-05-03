from django.contrib import admin
from apps.academy.models import Academy

# Register your models here.
@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['title']
    search_fields = ['title']