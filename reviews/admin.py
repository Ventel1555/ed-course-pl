from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'get_student_display', 'rating', 'created_at']
    list_filter = ['course', 'rating']
    search_fields = ['comment', 'student__username', 'course__title'] 

    def get_student_display(self, obj):
        return obj.student.username
    get_student_display.short_description = 'Student'