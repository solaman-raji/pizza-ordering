from rest_framework import serializers

from ..config import GenderType, CountryType


class CustomerSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(
        read_only=True,
    )
    first_name = serializers.CharField(
        max_length=100,
    )
    last_name = serializers.CharField(
        max_length=100,
    )
    gender = serializers.ChoiceField(
        choices=GenderType.CHOICES,
        allow_blank=True,
    )
    mobile_number = serializers.CharField(
        max_length=20,
    )
    email = serializers.EmailField(
        required=False,
        allow_blank=True,
    )
    zip_code = serializers.CharField(
        max_length=20,
        required=False,
        allow_blank=True,
    )
    house_number = serializers.CharField(
        required=False,
        max_length=20,
        allow_blank=True,
    )
    house_number_extension = serializers.CharField(
        max_length=20,
        required=False,
        allow_blank=True,
    )
    street = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )
    city = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )
    country = serializers.ChoiceField(
        required=False,
        choices=CountryType.CHOICES,
        default="DE",
    )
