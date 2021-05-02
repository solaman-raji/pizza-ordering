# Get All Orders API

Get all orders with pagination and filtering options.

**URL** : `/api/v1/orders/`

**Method** : `GET`

**Pagination** : 20 items per page

**Filter With** : flavour, size, quantity, delivery_status, first_name, last_name, mobile_number

**Filter URL Example** : `/api/v1/orders/?page=1&flavour=margarita&size=small&quantity=1&delivery_status=delivered&first_name=Patrick&last_name=Propst&mobile_number=0309829661`

## Success Response

**Code** : `200 OK`

**Content** :

```json
{
  "success": true,
  "meta": {},
  "message": "",
  "data": {
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
      {
        "uuid": "868f55a5-c411-4131-9fac-a4e033276af3",
        "flavour": "margarita",
        "size": "large",
        "quantity": 1,
        "delivery_status": "received",
        "created_at": "2021-05-02T17:10:30.624551+02:00",
        "customer": {
          "uuid": "e30a81ae-78c5-4dfc-badb-1e7dbec0d1f6",
          "first_name": "Patrick",
          "last_name": "Propst",
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
      },
      {
        "uuid": "245e7b8a-6b6a-4f2f-8c51-9a6f4dacdda2",
        "flavour": "margarita",
        "size": "medium",
        "quantity": 1,
        "delivery_status": "received",
        "created_at": "2021-05-02T17:10:27.724892+02:00",
        "customer": {
          "uuid": "e30a81ae-78c5-4dfc-badb-1e7dbec0d1f6",
          "first_name": "Patrick",
          "last_name": "Propst",
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
      },
      {
        "uuid": "97476d7f-73fc-4cf2-94ae-dedbeb777a6e",
        "flavour": "margarita",
        "size": "small",
        "quantity": 1,
        "delivery_status": "received",
        "created_at": "2021-05-02T17:10:18.914680+02:00",
        "customer": {
          "uuid": "e30a81ae-78c5-4dfc-badb-1e7dbec0d1f6",
          "first_name": "Patrick",
          "last_name": "Propst",
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
    ]
  }
}
```
