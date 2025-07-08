from rest_framework import serializers
from reviews.serializers import ReviewSerializer
from users.serializers import UserSerializer
from lessons.serializers import LessonSerializer
from .models import Course, Module, UserCourseProgress

class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'order', 'lessons']

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    first_lesson = serializers.SerializerMethodField()
    is_started = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'category', 'level', 'teacher', 'created_at', 'updated_at', 'modules', 'reviews', 'first_lesson', 'is_started']

    def get_first_lesson(self, obj):
        first_module = obj.modules.order_by('order').first()
        if first_module:
            first_lesson = first_module.lessons.order_by('order').first()
            if first_lesson:
                return LessonSerializer(first_lesson).data
        return None

    def get_is_started(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return UserCourseProgress.objects.filter(user=user, course=obj).exists()
        return False