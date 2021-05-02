# Delete Order API

Delete order.

**URL** : `/api/v1/orders/:order_uuid/`

**Method** : `DELETE`

## Success Response

**Code** : `200 OK`

**Content** :

```json
{
  "success": true,
  "meta": {},
  "message": "",
  "data": {
    "message": "Order deleted successfully"
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
