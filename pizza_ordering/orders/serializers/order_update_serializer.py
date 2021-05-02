from rest_framework import serializers

from pizza_ordering.customers.serializers import CustomerSerializer
from .order_serializer import OrderSerializer
from ..config import FlavourType, SizeType, DeliveryStatusType


class OrderUpdateSerializer(OrderSerializer):
    flavour = serializers.ChoiceField(required=False, choices=FlavourType.CHOICES)
    size = serializers.ChoiceField(required=False, choices=SizeType.CHOICES)
    quantity = serializers.IntegerField(required=False)
    delivery_status = serializers.ChoiceField(choices=DeliveryStatusType.CHOICES)
    customer = CustomerSerializer(read_only=True)
