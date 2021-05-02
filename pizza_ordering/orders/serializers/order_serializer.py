from rest_framework import serializers

from pizza_ordering.customers.serializers import CustomerSerializer
from ..config import FlavourType, SizeType, DeliveryStatusType


class OrderSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    flavour = serializers.ChoiceField(choices=FlavourType.CHOICES)
    size = serializers.ChoiceField(choices=SizeType.CHOICES)
    quantity = serializers.IntegerField()
    delivery_status = serializers.ChoiceField(read_only=True, choices=DeliveryStatusType.CHOICES)
    created_at = serializers.DateTimeField(read_only=True)
    customer = CustomerSerializer()
