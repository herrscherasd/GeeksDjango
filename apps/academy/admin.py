from django.contrib import admin
from apps.academy.models import Academy,SettingsModel,AboutModel,SlideModel,CourseModel

# Register your models here.
@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(SettingsModel)
admin.site.register(AboutModel)
admin.site.register(SlideModel)
admin.site.register(CourseModel)