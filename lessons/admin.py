from django.contrib import admin
from .models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'content_type', 'order']
    list_filter = ['module__course', 'content_type']
    search_fields = ['title', 'content']