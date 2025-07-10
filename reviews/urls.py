from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import CourseReviewViewSet

router = DefaultRouter()
router.register(r'courses/(?P<course_id>\d+)/reviews', CourseReviewViewSet, basename='course-reviews')

urlpatterns = [
    path('', include(router.urls)),
]