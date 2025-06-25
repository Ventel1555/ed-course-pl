from django.db import models
from django.contrib.auth.models import AbstractUser

# Кастомная модель пользователя с ролями (студент, преподаватель, администратор).
class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        if self.role == 'admin' and not self.is_superuser:
            raise ValueError("Only superusers can assign the 'admin' role.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
