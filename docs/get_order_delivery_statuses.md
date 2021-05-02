# Get Order Delivery Statuses

Get order delivery statuses.

**URL** : `/api/v1/orders/:order_uuid/delivery-statuses/`

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
    "results": [
      {
        "delivery_status": "delivered",
        "created_at": "2021-05-02T19:10:12.231297+02:00"
      },
      {
        "delivery_status": "out_for_delivery",
        "created_at": "2021-05-02T18:50:12.231297+02:00"
      },
      {
        "delivery_status": "processing",
        "created_at": "2021-05-02T18:30:12.231297+02:00"
      },
      {
        "delivery_status": "received",
        "created_at": "2021-05-02T17:49:12.231297+02:00"
      }
    ],
    "count": 4
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
