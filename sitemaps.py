from django.contrib.sitemaps import Sitemap
from courses.models import Course
from lessons.models import Lesson
from django.urls import reverse
from django.http import HttpRequest

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    # def items(self):
    #     return ['home', 'profile', 'courses_list']

    def location(self, item):
        return reverse(item)

class CourseSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Course.objects.all()

    def location(self, obj):
        return f"/api/courses/{obj.pk}/"

    def lastmod(self, obj):
        return obj.updated_at

class CourseReviewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Course.objects.all()

    def location(self, obj):
        return f"/api/courses/{obj.pk}/reviews/"

class LessonSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Lesson.objects.select_related('module__course').all()

    def location(self, obj):
        return f"/api/lessons/?course_id={obj.module.course.id}&module_id={obj.module.id}"

    def lastmod(self, obj):
        return obj.module.course.updated_at