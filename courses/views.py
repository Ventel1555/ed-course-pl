from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, UserCourseProgress
from .serializers import CourseSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        paginator = PageNumberPagination()
        paginated_courses = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(paginated_courses, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

class CourseDetailView(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

class CourseStartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            progress, created = UserCourseProgress.objects.get_or_create(
                user=request.user,
                course=course
            )
            return Response({'message': 'Course started', 'progress_id': progress.id}, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

class CourseLeaveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            progress = UserCourseProgress.objects.filter(user=request.user, course=course)
            if progress.exists():
                progress.delete()
                return Response(
                    {'message': 'Successfully left the course'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error': 'You are not enrolled in this course'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Course.DoesNotExist:
            return Response(
                {'error': 'Course not found'},
                status=status.HTTP_404_NOT_FOUND
            )