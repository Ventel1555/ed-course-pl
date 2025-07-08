from django.urls import path
from .views import CourseListView, CourseDetailView, CourseStartView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/start/', CourseStartView.as_view(), name='course-start'),
]