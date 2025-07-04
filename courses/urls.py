from django.urls import path, include
from .views import CourseDetailView, CourseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('', include(router.urls)),
]
