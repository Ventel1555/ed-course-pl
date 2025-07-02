from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'student', 'course', 'amount', 'status', 'created_at', 'transaction_id']
        read_only_fields = ['status', 'created_at', 'transaction_id']