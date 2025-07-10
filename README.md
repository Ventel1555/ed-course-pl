# EdTech Platform

A scalable online learning platform built with Django, designed for students, instructors, and administrators. The platform allows users to create, purchase, and take educational courses, with features like course management, payment integration, progress tracking, and reviews.

## COMANDS FOR DEV
- docker-compose down
- docker-compose up --build -d
- docker-compose exec web python manage.py runserver
- docker-compose exec web pip install -r requirements.txt

## URLS
- Пояснение:

    URL: /api/lessons/?course_id=1&module_id=2 — список уроков для модуля.
    URL: /api/lessons/<pk>/?course_id=1&module_id=2 — детали урока (с проверкой принадлежности курсу и модулю).
- 

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Architecture Decisions](#architecture-decisions)
- [License](#license)

## Features

### For Students
- Register and log in using email/password or Google/GitHub OAuth.
- Browse and filter courses by category, level, price, and rating.
- Access video lessons, text content, and quizzes.
- Track learning progress in a personal dashboard.
- Leave reviews and ratings for courses.

### For Instructors
- Create and manage courses with modules and lessons.
- Upload video and text-based content.
- Design quizzes with multiple-choice or open-ended questions.
- View course statistics (enrollments, revenue).
- Control student access to courses.

### For Administrators
- Manage users (block, change roles).
- Moderate courses (approve/reject).
- View platform analytics (revenue, active users).
- Manage course categories.

### Additional Features
- Full-text search for courses and instructors (PostgreSQL Full-Text Search or Elasticsearch).
- Email notifications for purchases, new lessons, and deadlines.
- Responsive UI with support for multiple languages (English, Russian).
- Secure payment processing and user authentication.

## Technologies

- **Backend**:
  - Django 5.x
  - Django REST Framework (DRF)
  - PostgreSQL
  - Celery + Redis (for asynchronous tasks like email notifications)
  - Django Channels (optional, for push notifications)
- **Frontend**:
  - Django Templates with Tailwind CSS or React/Vue.js SPA
  - JavaScript for interactive elements (e.g., video player)
- **Integrations**:
  - Google/GitHub OAuth for authentication
  - Vimeo/YouTube API for video hosting
  - Elasticsearch (optional, for advanced search)
- **DevOps**:
  - Docker + Docker Compose
  - Nginx + Gunicorn
  - Deployment on Heroku/AWS/DigitalOcean
- **Testing**:
  - Pytest/Django Test Framework (80%+ test coverage)

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL 15+
- Redis 7+
- Docker (optional, for containerized setup)
- Node.js (if using React/Vue.js frontend)

## Configuration

Create a `.env` file in the project root with the following variables:

```env
# Django settings
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/edtech_platform

# Redis
REDIS_URL=redis://localhost:6379/0

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password

# Stripe/PayPal
STRIPE_SECRET_KEY=your-stripe-secret-key
PAYPAL_CLIENT_ID=your-paypal-client-id
PAYPAL_SECRET=your-paypal-secret

# OAuth
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
```

Generate a `SECRET_KEY` using a secure random generator. For production, set `DEBUG=False` and configure `ALLOWED_HOSTS` appropriately.

## Running the Project

<!-- 2. Start Celery for asynchronous tasks:
   ```bash
   celery -A edtech_platform worker -l info
   ```

3. (Optional) Start Celery Beat for scheduled tasks:
   ```bash
   celery -A edtech_platform beat -l info
   ```

4. Access the platform at `http://localhost:8000`. -->

## API Documentation

<!-- The API is documented using Swagger/OpenAPI. After starting the server, access the documentation at:

```
http://localhost:8000/api/schema/swagger-ui/
```

Key endpoints:
- `/api/courses/` - List and filter courses
- `/api/courses/{id}/` - Course details
- `/api/enrollments/` - Manage course enrollments
- `/api/reviews/` - Manage reviews
- `/api/auth/` - Authentication and registration -->

## Deployment

### Using Docker
<!-- 1. Build and start containers:
   ```bash
   docker-compose up --build
   ```

2. Apply migrations inside the container:
   ```bash
   docker-compose exec web python manage.py migrate
   ``` -->

### Using Heroku/AWS/DigitalOcean
<!-- 1. Configure the platform-specific settings (e.g., database, Redis).
2. Deploy using Gunicorn and Nginx:
   ```bash
   gunicorn edtech_platform.wsgi:application --bind 0.0.0.0:8000
   ```

Refer to platform-specific guides for detailed steps. -->

## Project Structure

```
edtech-platform/
├── edtech_platform/       # Django project settings
├── courses/               # Course management app
├── users/                 # User management and authentication
├── payments/              # Payment processing (Stripe/PayPal)
├── lessons/               # Lesson and quiz management
├── reviews/               # Reviews and ratings
├── manage.py/
├── log_by_ai.txt/         # Info about current version by ai
├── static/                # Static files (CSS, JS)
├── templates/             # Django templates (or React/Vue.js build)
├── docker-compose.yml     # Docker configuration
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Architecture Decisions

- **Django + DRF**: Chosen for rapid development, robust ORM, and built-in security features.
- **PostgreSQL**: Scalable and supports full-text search for course discovery.
- **Celery + Redis**: Handles asynchronous tasks like email notifications and payment processing.
- **Tailwind CSS**: Simplifies responsive design with minimal custom CSS.
- **Docker**: Ensures consistent development and production environments.

## License

<!-- This project is licensed under the MIT License. See the `LICENSE` file for details. -->