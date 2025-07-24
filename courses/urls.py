from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    CourseStartView,
    CourseLeaveView,
    CourseViewSet,
    ModuleViewSet,
    CourseEditView,
    CourseListHTMLView,
    CourseDetailHTMLView
)

# CourseViewSet actions
course_viewset = CourseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
course_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

# ModuleViewSet actions
module_viewset = ModuleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
module_detail = ModuleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    # API endpoints
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/start/', CourseStartView.as_view(), name='course-start'),
    path('courses/<int:pk>/leave/', CourseLeaveView.as_view(), name='course-leave'),
    path('courses/create/', course_viewset, name='course-create'),
    path('courses/<int:pk>/edit/', course_detail, name='course-edit-api'),
    path('courses/<int:pk>/delete/', course_detail, name='course-delete'),
    path('courses/<int:course_id>/modules/', module_viewset, name='module-list'),
    path('courses/<int:course_id>/modules/<int:pk>/', module_detail, name='module-detail'),
    
    # HTML endpoints
    path('courses/list/', CourseListHTMLView.as_view(), name='course-list-html'),
    path('courses/<int:pk>/detail/', CourseDetailHTMLView.as_view(), name='course-detail-html'),
    path('courses/edit/', CourseEditView.as_view(), name='course-edit'),
]