from django.urls import path

from .views import OrderViewSet, OrderDeliveryStatusViewSet

app_name = "pizza_ordering.orders"

urlpatterns = [
    path(
        "",
        view=OrderViewSet.as_view({
            "get": "list",
            "post": "create",
        }),
        name="order-list-create"
    ),
    path(
        "<uuid:order_uuid>/",
        view=OrderViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "delete": "destroy",
        }),
        name="order-retrieve-update-destroy"
    ),
    path(
        "<uuid:order_uuid>/delivery-statuses/",
        view=OrderDeliveryStatusViewSet.as_view({
            "get": "list",
        }),
        name="order-delivery-status-list"
    ),
]
