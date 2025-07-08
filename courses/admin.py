from django.contrib import admin
from .models import Course, Module, Enrollment, UserCourseProgress
from lessons.models import Lesson

# Inline для уроков в модуле
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ['title', 'content_type', 'content', 'order']

# Inline для модулей в курсе
class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1
    fields = ['title', 'order']
    inlines = [LessonInline]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'category', 'level', 'price', 'created_at']
    list_filter = ['category', 'level', 'teacher']
    search_fields = ['title', 'description']
    inlines = [ModuleInline]
    fieldsets = (
        (None, {'fields': ('title', 'description', 'teacher')}),
        ('Details', {'fields': ('price', 'category', 'level')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    readonly_fields = ['created_at', 'updated_at'] 

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_filter = ['course']
    search_fields = ['title']
    inlines = [LessonInline]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'purchase_date', 'progress']
    list_filter = ['course', 'purchase_date']
    search_fields = ['student__username', 'course__title']

@admin.register(UserCourseProgress)
class UserCourseProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'started_at']
    list_filter = ['course', 'user']
    filter_horizontal = ['completed_lessons']
    search_fields = ['user__username', 'course__title']