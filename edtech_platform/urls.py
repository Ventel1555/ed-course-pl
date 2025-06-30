from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminbuilder/', admin.site.urls),
    path('api/', include('courses.urls')),
    path('', include('payments.urls')),
    path('', include('users.urls')),
]