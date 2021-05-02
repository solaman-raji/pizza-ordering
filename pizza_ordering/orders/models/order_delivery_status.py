from django.db import models
from django.utils.translation import gettext_lazy as _

from pizza_ordering.common.models import AbstractBaseModel
from .order import Order
from ..config import DeliveryStatusType


class OrderDeliveryStatus(AbstractBaseModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="delivery_statuses",
        verbose_name=_("Order"),
        help_text=_("Order"),
    )
    delivery_status = models.CharField(
        max_length=20,
        choices=DeliveryStatusType.CHOICES,
        default=DeliveryStatusType.RECEIVED,
        verbose_name=_("Delivery Status"),
        help_text=_("Delivery status of the order"),
    )

    def __str__(self):
        return f"{self.order.uuid} - {self.delivery_status}"
