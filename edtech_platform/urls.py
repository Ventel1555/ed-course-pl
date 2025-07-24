from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from sitemaps import StaticSitemap, CourseSitemap, CourseReviewsSitemap, LessonSitemap

sitemaps = {
    'static': StaticSitemap,
    'courses': CourseSitemap,
    'reviews': CourseReviewsSitemap,
    'lessons': LessonSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
    path('api/', include('lessons.urls')),
    path('about/', include('reviews.urls')),
    path('users/', include('users.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]