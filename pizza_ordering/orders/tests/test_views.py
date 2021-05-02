import json

from django.conf import settings
from django.urls import reverse
from rest_framework import status

from pizza_ordering.orders.config import DeliveryStatusType
from pizza_ordering.orders.models import Order, OrderDeliveryStatus


class TestOrderViewSet:
    order_list_create_endpoint = reverse(
        f"{settings.API_VERSION_NAMESPACE}:orders:order-list-create"
    )

    def test_order_list(self, use_fixtures, client):
        response = client.get(path=self.order_list_create_endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert response.data["count"] == 3

    def test_order_create(self, use_fixtures, client, order_create_payload):
        response = client.post(
            path=self.order_list_create_endpoint,
            content_type="application/json",
            data=json.dumps(order_create_payload),
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data

        order_uuid = response.data["uuid"]
        order_delivery_statuses = OrderDeliveryStatus.objects.filter(order__uuid=order_uuid)

        assert order_delivery_statuses
        assert order_delivery_statuses.count() == 1
        assert order_delivery_statuses[0].delivery_status == DeliveryStatusType.RECEIVED

    def test_order_create_without_order_data(self, use_fixtures, client, order_create_payload):
        order_create_payload.pop("flavour")
        order_create_payload.pop("size")
        order_create_payload.pop("quantity")

        response = client.post(
            path=self.order_list_create_endpoint,
            content_type="application/json",
            data=json.dumps(order_create_payload),
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_order_create_without_customer_object(self, use_fixtures, client, order_create_payload):
        order_create_payload.pop("customer")

        response = client.post(
            path=self.order_list_create_endpoint,
            content_type="application/json",
            data=json.dumps(order_create_payload),
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_order_create_without_customer_data(self, use_fixtures, client, order_create_payload):
        order_create_payload["customer"].pop("first_name")
        order_create_payload["customer"].pop("last_name")
        order_create_payload["customer"].pop("mobile_number")

        response = client.post(
            path=self.order_list_create_endpoint,
            content_type="application/json",
            data=json.dumps(order_create_payload),
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_order_create_duplicate(self, use_fixtures, client, order_create_payload):
        order_create_payload["size"] = "small"
        response = client.post(
            path=self.order_list_create_endpoint,
            content_type="application/json",
            data=json.dumps(order_create_payload),
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_retrieve_order(self, use_fixtures, client):
        order = Order.objects.get(id=1)
        order_retrieve_update_destroy_endpoint = reverse(
            f"{settings.API_VERSION_NAMESPACE}:orders:order-retrieve-update-destroy",
            kwargs={"order_uuid": order.uuid},
        )
        response = client.get(order_retrieve_update_destroy_endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert response.data["flavour"] == "margarita"
        assert response.data["size"] == "small"
        assert response.data["quantity"] == 1
        assert response.data["customer"]["uuid"] == str(order.customer.uuid)

        order_delivery_statuses = OrderDeliveryStatus.objects.filter(order__uuid=order.uuid)

        assert order_delivery_statuses
        assert order_delivery_statuses.count() == 1
        assert order_delivery_statuses[0].delivery_status == DeliveryStatusType.RECEIVED

    def test_retrieve_order_does_not_exist(self, use_fixtures, client):
        order_retrieve_update_destroy_endpoint = reverse(
            f"{settings.API_VERSION_NAMESPACE}:orders:order-retrieve-update-destroy",
            kwargs={"order_uuid": "9fbf24e7-fb1d-4a47-8c35-c0dfb942d3e4"},
        )
        response = client.get(order_retrieve_update_destroy_endpoint)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_update_order(self, use_fixtures, client, order_update_payload):
        order_id = 1
        order = Order.objects.get(id=order_id)

        order_retrieve_update_destroy_endpoint = reverse(
            f"{settings.API_VERSION_NAMESPACE}:orders:order-retrieve-update-destroy",
            kwargs={"order_uuid": order.uuid},
        )
        response = client.put(
            path=order_retrieve_update_destroy_endpoint,
            content_type="application/json",
            data=json.dumps(order_update_payload),
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert response.data["flavour"] == "marinara"
        assert response.data["size"] == "medium"
        assert response.data["quantity"] == 2
        assert response.data["delivery_status"] == "processing"

        order_delivery_statuses = OrderDeliveryStatus.objects.filter(order_id=order_id)

        assert order_delivery_statuses
        assert order_delivery_statuses.count() == 2
        assert order_delivery_statuses[0].delivery_status == DeliveryStatusType.RECEIVED
        assert order_delivery_statuses[1].delivery_status == DeliveryStatusType.PROCESSING

    def test_update_order_does_not_exist(self, use_fixtures, client, order_update_payload):
        order_retrieve_update_destroy_endpoint = reverse(
            f"{settings.API_VERSION_NAMESPACE}:orders:order-retrieve-update-destroy",
            kwargs={"order_uuid": "9fbf24e7-fb1d-4a47-8c35-c0dfb942d3e4"},
        )
        response = client.put(
            path=order_retrieve_update_destroy_endpoint,
            content_type="application/json",
            data=json.dumps(order_update_payload),
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_update_order_already_delivered(self, use_fixtures, client, order_update_payload):
        order_id = 1
        order = Order.objects.get(id=order_id)
        order.delivery_status = "delivered"
        order.save()

        order_retrieve_update_destroy_endpoint = reverse(
            f"{settings.API_VERSION_NAMESPACE}:orders:order-retrieve-update-destroy",
            kwargs={"order_uuid": order.uuid},
        )
        response = client.put(
            path=order_retrieve_update_destroy_endpoint,
            content_type="application/json",
            data=json.dumps(order_update_payload),
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_destroy_order(self, use_fixtures, client):
        order_id = 1
        order = Order.objects.get(id=order_id)

        order_retrieve_update_destroy_endpoint = reverse(
            f"{settings.API_VERSION_NAMESPACE}:orders:order-retrieve-update-destroy",
            kwargs={"order_uuid": order.uuid},
        )
        response = client.delete(order_retrieve_update_destroy_endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert Order.objects.all().count() == 2
        assert not OrderDeliveryStatus.objects.filter(order_id=order_id)

    def test_destroy_order_does_not_exist(self, use_fixtures, client):
        order_retrieve_update_destroy_endpoint = reverse(
            f"{settings.API_VERSION_NAMESPACE}:orders:order-retrieve-update-destroy",
            kwargs={"order_uuid": "9fbf24e7-fb1d-4a47-8c35-c0dfb942d3e4"},
        )
        response = client.delete(order_retrieve_update_destroy_endpoint)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestOrderDeliveryStatusViewSet:

    def test_order_delivery_status_list(self, use_fixtures, client):
        order_id = 1
        order = Order.objects.get(id=order_id)

        order_delivery_status_list_endpoint = reverse(
            f"{settings.API_VERSION_NAMESPACE}:orders:order-delivery-status-list",
            kwargs={"order_uuid": order.uuid},
        )
        response = client.get(path=order_delivery_status_list_endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert len(response.data) == 1
