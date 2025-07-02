from django.urls import path
from .views import CreatePaymentView, payment_success, payment_webhook

urlpatterns = [
    path('api/payments/create/', CreatePaymentView.as_view(), name='create-payment'),
    path('payment/success/', payment_success, name='payment-success'),
    path('api/payments/webhook/', payment_webhook, name='payment-webhook'),
]
