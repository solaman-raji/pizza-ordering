from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from .filters import OrderListFilter
from .models import Order
from .paginations import OrderListPagination
from .serializers import (
    OrderSerializer,
    OrderUpdateSerializer,
    OrderDeliveryStatusSerializer,
)
from .services import OrderService, OrderDeliveryStatusService


class OrderViewSet(viewsets.ViewSet, generics.ListAPIView):
    filterset_class = OrderListFilter
    pagination_class = OrderListPagination
    serializer_class = OrderSerializer
    order_update_serializer_class = OrderUpdateSerializer
    service_class = OrderService

    def get_queryset(self):
        return Order.objects.filter().order_by("-created_at")

    def create(self, request):
        input_serializer = self.serializer_class(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        order_service = self.service_class()
        order = order_service.create_order(order_data=input_serializer.data)

        output_serializer = self.serializer_class(order)

        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, order_uuid):
        order_service = self.service_class()
        order = order_service.get_order(order_uuid)

        output_serializer = self.serializer_class(order)

        return Response(data=output_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, order_uuid):
        input_serializer = self.order_update_serializer_class(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        order_service = self.service_class()
        order = order_service.update_order(
            order_uuid=order_uuid,
            order_data=input_serializer.data,
        )

        output_serializer = self.serializer_class(order)

        return Response(data=output_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, order_uuid):
        order_service = self.service_class()
        order_service.delete_order(order_uuid)

        data = {
            "message": "Order deleted successfully"
        }

        return Response(data=data, status=status.HTTP_200_OK)


class OrderDeliveryStatusViewSet(viewsets.ViewSet):
    serializer_class = OrderDeliveryStatusSerializer
    service_class = OrderDeliveryStatusService

    def list(self, request, order_uuid):
        order_delivery_status_service = self.service_class()
        order_delivery_statuses = order_delivery_status_service.get_order_delivery_statuses(order_uuid)

        output_serializer = self.serializer_class(order_delivery_statuses, many=True)

        return Response(data=output_serializer.data, status=status.HTTP_200_OK)
