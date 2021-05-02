# REST API Docs

Where full URLs are not provided those will be rendered as if service
is running on 'http://localhost:8000/'.

### Order APIs

APIs for viewing and manipulating orders.

* [Get All Orders](get_all_orders.md) : `GET /api/v1/orders/`
* [Create Order](create_order.md) : `POST /api/v1/orders/`
* [Get Order](get_order.md) : `GET /api/v1/orders/:order_uuid/`
* [Update Order](update_order.md) : `PUT /api/v1/orders/:order_uuid/`
* [Delete Order](delete_order.md) : `DELETE /api/v1/orders/:order_uuid/`
* [Get Order Delivery Statuses](get_order_delivery_statuses.md) : `GET /api/v1/orders/:order_uuid/delivery-statuses`
