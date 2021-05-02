from django.db import transaction

from pizza_ordering.customers.services import CustomerService
from .order_delivery_status_service import OrderDeliveryStatusService
from ..config import DeliveryStatusType
from ..exceptions import (
    DuplicateOrderException,
    OrderAlreadyDeliveredException,
    order_exceptions,
)
from ..models import Order


class OrderService:
    """
    Order Service
    """
    model = Order

    def _check_duplicate_order(self, order_data):
        """
        Check Duplicate Order
        :param order_data: Order payload
        :return: None
        """
        customer = order_data.get("customer")
        flavour = order_data.get("flavour")
        size = order_data.get("size")
        mobile_number = customer.get("mobile_number")

        if self.model.objects.filter(
            flavour=flavour,
            size=size,
            customer__mobile_number=mobile_number,
        ).exists():
            raise DuplicateOrderException

    def create_order(self, order_data):
        """
        Create Order
        :param order_data: Order payload
        :return: order: Order object
        """
        # If duplicate order raise error
        self._check_duplicate_order(order_data)
        customer_data = order_data.pop("customer")

        with transaction.atomic(), order_exceptions():
            mobile_number = customer_data.pop("mobile_number")

            # Create customer
            customer_service = CustomerService()
            customer, created = customer_service.get_or_create(mobile_number, customer_data)

            # Create order
            order_data["customer_id"] = customer.id
            order = self.model.objects.create(**order_data)

            # Create order delivery status
            order_delivery_status_data = {
                "order_id": order.id,
                "delivery_status": order.delivery_status,
            }
            order_delivery_status_service = OrderDeliveryStatusService()
            order_delivery_status_service.create_order_delivery_status(order_delivery_status_data)

        return order

    def get_order(self, order_uuid):
        """
        Get Order
        :param order_uuid: Order UUID
        :return: order: Order object
        """
        with order_exceptions():
            order = self.model.objects.get(uuid=order_uuid)

        return order

    def update_order(self, order_uuid, order_data):
        """
        Update Order
        :param order_uuid: Order UUID
        :param order_data: Order payload
        :return: order: Order object
        """
        with order_exceptions():
            order = self.model.objects.get(uuid=order_uuid)

        # If delivered order cannot be updated anymore
        if order.delivery_status == DeliveryStatusType.DELIVERED:
            raise OrderAlreadyDeliveredException

        with transaction.atomic(), order_exceptions():
            has_order_delivery_status_changed = False
            order_flavour = order_data.get("flavour")
            order_size = order_data.get("size")
            order_quantity = order_data.get("quantity")
            order_delivery_status = order_data.get("delivery_status")

            if order_flavour:
                order.flavour = order_flavour

            if order_size:
                order.size = order_size

            if order_quantity:
                order.quantity = order_quantity

            if order_delivery_status:
                if order_delivery_status != order.delivery_status:
                    has_order_delivery_status_changed = True

                order.delivery_status = order_delivery_status

            order.save()
            order.refresh_from_db()

            # If delivery_status has changed create order delivery status entry
            if has_order_delivery_status_changed:
                order_delivery_status_data = {
                    "order_id": order.id,
                    "delivery_status": order.delivery_status,
                }
                order_delivery_status_service = OrderDeliveryStatusService()
                order_delivery_status_service.create_order_delivery_status(order_delivery_status_data)

        return order

    def delete_order(self, order_uuid):
        """
        Update Order
        :param order_uuid: Order UUID
        :return: None
        """
        with transaction.atomic(), order_exceptions():
            order = self.model.objects.get(uuid=order_uuid)
            order.delete()
