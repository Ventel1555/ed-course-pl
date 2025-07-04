from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Course
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CoursePagination(PageNumberPagination):
    page_size = 10

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all().select_related('teacher')
    serializer_class = CourseSerializer
    pagination_class = CoursePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'level', 'price']