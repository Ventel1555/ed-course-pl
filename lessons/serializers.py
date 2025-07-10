from rest_framework import serializers
from .models import Lesson
from courses.models import Module, Course

class LessonSerializer(serializers.ModelSerializer):
    module = serializers.StringRelatedField()
    course = serializers.StringRelatedField(source='module.course')
    next_lesson = serializers.SerializerMethodField()
    previous_lesson = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['id', 'module', 'course', 'title', 'content_type', 'content', 'order', 'next_lesson', 'previous_lesson']

    def get_next_lesson(self, obj):
        next_lesson = Lesson.objects.filter(module=obj.module, order__gt=obj.order).order_by('order').first()
        if next_lesson:
            return {'id': next_lesson.id, 'title': next_lesson.title}
        return None

    def get_previous_lesson(self, obj):
        previous_lesson = Lesson.objects.filter(module=obj.module, order__lt=obj.order).order_by('-order').first()
        if previous_lesson:
            return {'id': previous_lesson.id, 'title': previous_lesson.title}
        return None