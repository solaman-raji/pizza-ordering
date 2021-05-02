import pytest
from django.core.management import call_command


@pytest.fixture
def use_fixtures():
    call_command("loaddata", "orders.json")


@pytest.fixture
def order_create_payload():
    return {
        "flavour": "margarita",
        "size": "medium",
        "quantity": 1,
        "customer": {
            "first_name": "Patrick1",
            "last_name": "Propst1",
            "gender": "M",
            "mobile_number": "0309829661",
            "email": "nx0xw0a45cs1@temporary-mail.net",
            "zip_code": "13359",
            "house_number": "10",
            "house_number_extension": "A",
            "street": "Wedding",
            "city": "Berlin",
            "country": "DE"
        }
    }


@pytest.fixture
def order_update_payload():
    return {
        "flavour": "marinara",
        "size": "medium",
        "quantity": 2,
        "delivery_status": "processing"
    }
