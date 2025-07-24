from django.urls import path
from .views import LessonViewSet, LessonListHTMLView
from reviews.views import CourseReviewViewSet, CourseReviewHTMLView

# LessonViewSet actions
lesson_viewset = LessonViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
lesson_detail = LessonViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

# CourseReviewViewSet actions
review_viewset = CourseReviewViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    # API endpoints
    path('lessons/', lesson_viewset, name='lesson-list'),
    path('lessons/<int:pk>/', lesson_detail, name='lesson-detail'),
    path('courses/<int:course_id>/reviews/', review_viewset, name='course-reviews'),
    
    # HTML endpoints
    path('lessons/list/', LessonListHTMLView.as_view(), name='lesson-list-html'),
    path('courses/<int:course_id>/reviews/list/', CourseReviewHTMLView.as_view(), name='course-reviews-html'),
]