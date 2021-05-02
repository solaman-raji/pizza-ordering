# Get Order API

Get order.

**URL** : `/api/v1/orders/:order_uuid/`

**Method** : `GET`

## Success Response

**Code** : `200 OK`

**Content** :

```json
{
  "success": true,
  "meta": {},
  "message": "",
  "data": {
    "uuid": "864c8c57-cf36-4215-9bce-b23429aac365",
    "flavour": "margarita",
    "size": "small",
    "quantity": 1,
    "delivery_status": "received",
    "created_at": "2021-05-02T16:11:00.915862+02:00",
    "customer": {
      "uuid": "b87bc8d9-e48c-4fb6-bb24-6c1862208ea6",
      "first_name": "Solaman",
      "last_name": "Raji",
      "gender": "M",
      "mobile_number": "01676122579",
      "email": "solamanraji41@gmail.com",
      "zip_code": "1209",
      "house_number": "128",
      "house_number_extension": "4",
      "street": "Sultangong",
      "city": "Dhaka",
      "country": "BD"
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
    "error_code": "ORDER_DOES_NOT_EXIST",
    "message": "Order does not exist"
  },
  "message": ""
}
```
