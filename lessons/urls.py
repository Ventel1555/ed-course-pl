from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import CourseReviewViewSet
from lessons.views import LessonViewSet

router = DefaultRouter()
router.register(r'courses/(?P<course_id>\d+)/reviews', CourseReviewViewSet, basename='course-reviews')
router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = [
    path('', include(router.urls)),
]