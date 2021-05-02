from django_filters import FilterSet, CharFilter

from ..models import Order


class OrderListFilter(FilterSet):
    first_name = CharFilter(field_name="customer__first_name")
    last_name = CharFilter(field_name="customer__last_name")
    mobile_number = CharFilter(field_name="customer__mobile_number")

    class Meta:
        model = Order
        fields = [
            "flavour",
            "size",
            "quantity",
            "delivery_status",
        ]
