from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()

teacher = User.objects.create_user(
    username='Skebob',
    email='teacher@example.com',
    password='pass123',
    role='teacher'
)

Course.objects.create(
    title='Python для начинающих',
    description='Основы программирования на Python',
    price=0.00,
    category='Программирование',
    level='beginner',
    teacher=teacher
)
Course.objects.create(
    title='UI/UX Дизайн',
    description='Создание удобных интерфейсов',
    price=5000.00,
    category='Дизайн',
    level='intermediate',
    teacher=teacher
)
Course.objects.create(
    title='Машинное обучение',
    description='Продвинутые алгоритмы ML',
    price=10000.00,
    category='Программирование',
    level='advanced',
    teacher=teacher
)