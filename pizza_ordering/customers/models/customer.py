from django.db import models
from django.utils.translation import gettext_lazy as _

from pizza_ordering.common.models import BaseModel
from ..config import GenderType, CountryType


class Customer(BaseModel):
    first_name = models.CharField(
        max_length=100,
        verbose_name=_("First Name"),
        help_text=_("First name of the customer"),
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_("Last Name"),
        help_text=_("Last name of the customer"),
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderType.CHOICES,
        blank=True,
        verbose_name=_("Gender"),
        help_text=_("Gender of the customer"),
    )
    mobile_number = models.CharField(
        max_length=20,
        verbose_name=_("Mobile Number"),
        help_text=_("Mobile number of the customer"),
    )
    email = models.EmailField(
        blank=True,
        verbose_name=_("Email"),
        help_text=_("Email of the customer"),
    )
    zip_code = models.CharField(
        max_length=20,
        blank=True,
        default="",
        verbose_name=_("ZIP Code"),
        help_text=_("ZIP code of the customer"),
    )
    house_number = models.CharField(
        max_length=20,
        blank=True,
        default="",
        verbose_name=_("House Number"),
        help_text=_("House number of the customer"),
    )
    house_number_extension = models.CharField(
        max_length=20,
        blank=True,
        default="",
        verbose_name=_("House Number Extension"),
        help_text=_("House number extension of the customer"),
    )
    street = models.CharField(
        max_length=100,
        blank=True,
        default="",
        verbose_name=_("Street Name"),
        help_text=_("Street name of the customer"),
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        default="",
        verbose_name=_("City"),
        help_text=_("City of the customer"),
    )
    country = models.CharField(
        max_length=64,
        choices=CountryType.CHOICES,
        default="DE",
        verbose_name=_("Country"),
        help_text=_("Country of the customer"),
    )

    def __str__(self):
        return f"{self.uuid} - {self.first_name} {self.last_name}"
