from django.contrib import admin
from .models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'name',
        'bio',
    )

    ordering = ('name',)

admin.site.register(Teacher, TeacherAdmin)