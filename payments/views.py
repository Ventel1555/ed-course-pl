from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from yookassa import Configuration, Payment as YooPayment
from yookassa.domain.notification import WebhookNotification
from .models import Payment
from .serializers import PaymentSerializer
from courses.models import Course
import uuid

class CreatePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        course_id = request.data.get('course_id')
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)

        # Заглушка для тестирования без ключей
        if settings.YOOKASSA_SHOP_ID == 'placeholder_shop_id':
            payment_obj = Payment.objects.create(
                student=request.user,
                course=course,
                amount=course.price,
                transaction_id=f"test_{uuid.uuid4()}",
                status='pending'
            )
            return JsonResponse({
                'payment_url': 'http://localhost:8080/payment/success/',
                'payment_id': payment_obj.id,
                'message': 'Test mode: real payment skipped'
            })

        Configuration.account_id = settings.YOOKASSA_SHOP_ID
        Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

        payment = YooPayment.create(
            {
                "amount": {
                    "value": str(course.price),
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "http://localhost:8080/payment/success/"
                },
                "capture": True,
                "description": f"Payment for course {course.title}",
                "metadata": {"course_id": str(course_id), "user_id": str(request.user.id)}
            },
            idempotency_key=str(uuid.uuid4())
        )

        payment_obj = Payment.objects.create(
            student=request.user,
            course=course,
            amount=course.price,
            transaction_id=payment.id,
            status='pending'
        )

        return JsonResponse({
            'payment_url': payment.confirmation.confirmation_url,
            'payment_id': payment_obj.id
        })

def payment_success(request):
    return render(request, 'templates/payments/success.html')

@csrf_exempt
def payment_webhook(request):
    if request.method == 'POST':
        try:
            event_json = request.body.decode('utf-8')
            webhook_notification = WebhookNotification(event_json)
            payment = webhook_notification.object

            if payment.event == 'payment.succeeded':
                Payment.objects.filter(transaction_id=payment.id).update(status='completed')
            elif payment.event == 'payment.canceled':
                Payment.objects.filter(transaction_id=payment.id).update(status='failed')

            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(status=400)
    return HttpResponse(status=405)