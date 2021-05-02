from rest_framework import serializers

from ..config import DeliveryStatusType


class OrderDeliveryStatusSerializer(serializers.Serializer):
    delivery_status = serializers.ChoiceField(read_only=True, choices=DeliveryStatusType.CHOICES)
    created_at = serializers.DateTimeField(read_only=True)
