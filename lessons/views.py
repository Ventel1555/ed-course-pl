from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Lesson
from .serializers import LessonSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from courses.models import Course
from courses.views import IsTeacher
from django.shortcuts import render
from rest_framework.views import APIView

class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def get_queryset(self):
        course_id = self.request.query_params.get('course_id')
        module_id = self.request.query_params.get('module_id')
        if not course_id or not module_id:
            raise NotFound("Both course_id and module_id are required.")
        return Lesson.objects.filter(module__course_id=course_id, module_id=module_id)

    def perform_create(self, serializer):
        course = Course.objects.get(pk=self.request.query_params.get('course_id'))
        if self.request.user != course.teacher:
            raise PermissionDenied("Only the course teacher can create lessons.")
        serializer.save()

    def perform_update(self, serializer):
        course = Course.objects.get(pk=self.request.query_params.get('course_id'))
        if self.request.user != course.teacher:
            raise PermissionDenied("Only the course teacher can edit lessons.")
        serializer.save()

    def perform_destroy(self, instance):
        course = Course.objects.get(pk=self.request.query_params.get('course_id'))
        if self.request.user != instance.module.course.teacher:
            raise PermissionDenied("Only the course teacher can delete lessons.")
        instance.delete()

    def get_object(self):
        lesson_id = self.kwargs.get('pk')
        queryset = self.get_queryset()
        try:
            return queryset.get(pk=lesson_id)
        except Lesson.DoesNotExist:
            raise NotFound("Lesson not found.")

class LessonListHTMLView(APIView):
    def get(self, request):
        return render(request, 'lessons/list.html')