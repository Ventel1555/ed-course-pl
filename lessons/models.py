from django.db import models
from courses.models import Module

# Уроки (видео, текст, тесты).
class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50, choices=[('video', 'Video'), ('text', 'Text'), ('quiz', 'Quiz')])
    content = models.TextField()  # Ссылка на видео или текст или само содержание
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.module.title} - {self.title}"