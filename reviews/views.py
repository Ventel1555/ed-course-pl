from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.exceptions import NotFound
from django.shortcuts import render
from rest_framework.views import APIView

class CourseReviewViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        if not course_id:
            raise NotFound("Course ID is required.")
        return Review.objects.filter(course_id=course_id).order_by('-created_at')

class CourseReviewHTMLView(APIView):
    def get(self, request, course_id):
        return render(request, 'reviews/list.html')