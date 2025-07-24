from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, UserCourseProgress, Module
from .serializers import CourseSerializer, ModuleSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import render

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        paginator = PageNumberPagination()
        paginated_courses = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(paginated_courses, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

class CourseListHTMLView(APIView):
    def get(self, request):
        return render(request, 'courses/list.html')

class CourseDetailView(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

class CourseDetailHTMLView(APIView):
    def get(self, request, pk):
        return render(request, 'courses/detail.html')

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

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def perform_create(self, serializer):
        if self.request.user.role != 'teacher':
            raise PermissionDenied("Only teachers can create courses.")
        serializer.save(teacher=self.request.user)

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.teacher:
            raise PermissionDenied("Only the course teacher can edit this course.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.teacher:
            raise PermissionDenied("Only the course teacher can delete this course.")
        instance.delete()

class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Module.objects.filter(course_id=course_id)

    def perform_create(self, serializer):
        course = Course.objects.get(pk=self.kwargs['course_id'])
        if self.request.user != course.teacher:
            raise PermissionDenied("Only the course teacher can create modules.")
        serializer.save(course=course)

class CourseEditView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        courses = Course.objects.filter(teacher=request.user)
        return render(request, 'course_edit.html', {'courses': courses})