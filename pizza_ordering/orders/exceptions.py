from contextlib import contextmanager

from rest_framework import status

from pizza_ordering.orders.models import Order
from pizza_ordering.rest_utils.exceptions import BaseException, BadRequestException


class OrderDoesNotExistException(BaseException):
    errors = {
        "error_code": "ORDER_DOES_NOT_EXIST",
        "message": "Order does not exist",
    }
    status_code = status.HTTP_400_BAD_REQUEST


class DuplicateOrderException(BaseException):
    errors = {
        "error_code": "DUPLICATE_ORDER",
        "message": "Duplicate order",
    }
    status_code = status.HTTP_400_BAD_REQUEST


class OrderAlreadyDeliveredException(BaseException):
    errors = {
        "error_code": "ORDER_ALREADY_DELIVERED",
        "message": "Order already delivered",
    }
    status_code = status.HTTP_400_BAD_REQUEST


@contextmanager
def order_exceptions():
    try:
        yield
    except Order.DoesNotExist:
        raise OrderDoesNotExistException
    except Exception as e:
        raise BadRequestException(errors=str(e))
