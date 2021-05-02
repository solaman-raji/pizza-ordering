# Create Order API

Create an order for the customer.

**URL** : `/api/v1/orders/`

**Method** : `POST`

**Request Payload**

```json
{
  "flavour": "margarita",
  "size": "small",
  "quantity": 1,
  "customer": {
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
```

## Success Response

**Code** : `201 CREATED`

**Content** :

```json
{
  "success": true,
  "meta": {},
  "message": "",
  "data": {
    "uuid": "868f55a5-c411-4131-9fac-a4e033276af3",
    "flavour": "margarita",
    "size": "small",
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
  }
}
```

## Error Responses

**Code** : `400 Bad Request`

**Content** : 
```json
{
    "success": false,
    "error": {
        "error_code": "DUPLICATE_ORDER",
        "message": "Duplicate order"
    },
    "message": ""
}
```
