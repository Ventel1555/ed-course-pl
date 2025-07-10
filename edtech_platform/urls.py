from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
    path('study/', include('lessons.urls')),
    path('about/', include('reviews.urls')),
    path('', include('users.urls')),
]
