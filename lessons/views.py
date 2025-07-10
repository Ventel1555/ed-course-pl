from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Lesson
from .serializers import LessonSerializer
from rest_framework.exceptions import NotFound

class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.request.query_params.get('course_id')
        module_id = self.request.query_params.get('module_id')
        if not course_id or not module_id:
            raise NotFound("Both course_id and module_id are required.")
        return Lesson.objects.filter(module__course_id=course_id, module_id=module_id).order_by('order')

    def get_object(self):
        lesson_id = self.kwargs.get('pk')
        queryset = self.get_queryset()
        try:
            return queryset.get(pk=lesson_id)
        except Lesson.DoesNotExist:
            raise NotFound("Lesson not found.")