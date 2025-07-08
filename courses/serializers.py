from rest_framework import serializers
from reviews.serializers import ReviewSerializer
from users.serializers import UserSerializer
from .models import Course
from lessons.serializers import LessonSerializer
from .models import Course, Module

class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'order', 'lessons']
        

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'category', 'level', 'teacher', 'created_at', 'updated_at', 'modules', 'reviews']

