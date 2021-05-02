from django.db import models
from django.utils.translation import gettext_lazy as _

from pizza_ordering.common.models import BaseModel
from pizza_ordering.customers.models import Customer
from ..config import FlavourType, SizeType, DeliveryStatusType


class Order(BaseModel):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("Customer"),
        help_text=_("The customer who placed the order"),
    )
    flavour = models.CharField(
        max_length=20,
        choices=FlavourType.CHOICES,
        verbose_name=_("Flavour"),
        help_text=_("Flavour of the pizza"),
    )
    size = models.CharField(
        max_length=20,
        choices=SizeType.CHOICES,
        verbose_name=_("Size"),
        help_text=_("Size of the pizza"),
    )
    quantity = models.IntegerField(
        verbose_name=_("Quantity"),
        help_text=_("Quantity of the order"),
    )
    delivery_status = models.CharField(
        max_length=20,
        choices=DeliveryStatusType.CHOICES,
        default=DeliveryStatusType.RECEIVED,
        verbose_name=_("Delivery Status"),
        help_text=_("Delivery status of the order"),
    )

    def __str__(self):
        return f"{self.uuid} - {self.customer.first_name} {self.customer.last_name}"
