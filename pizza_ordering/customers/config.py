import pycountry
from django.utils.translation import gettext_lazy as _


class GenderType:
    MALE = "M"
    FEMALE = "F"
    UNKNOWN = "X"

    CHOICES = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
        (UNKNOWN, _("Unknown"))
    )


class CountryType:
    CHOICES = [(country.alpha_2, country.name) for country in list(pycountry.countries)]
