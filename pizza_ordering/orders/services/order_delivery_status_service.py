from ..models import OrderDeliveryStatus


class OrderDeliveryStatusService:
    """
    Order Delivery Status Service
    """
    model = OrderDeliveryStatus

    def get_order_delivery_statuses(self, order_uuid):
        """
        Get Order Delivery Statuses
        :param order_uuid: Order UUID
        :return: order_delivery_statuses: Order delivery status list
        """
        order_delivery_statuses = self.model.objects.filter(
            order__uuid=order_uuid
        ).order_by("-created_at")

        return order_delivery_statuses

    def create_order_delivery_status(self, order_delivery_status_data):
        """
        Create Order Delivery Status
        :param order_delivery_status_data: Order delivery status data
        :return: order_delivery_status: Order delivery status object
        """
        order_delivery_status = self.model.objects.create(**order_delivery_status_data)

        return order_delivery_status
