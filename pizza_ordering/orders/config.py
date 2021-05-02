class FlavourType:
    MARGARITA = "margarita"
    MARINARA = "marinara"
    SALAMI = "salami"

    CHOICES = (
        (MARGARITA, "Margarita"),
        (MARINARA, "Marinara"),
        (SALAMI, "Salami")
    )


class SizeType:
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

    CHOICES = (
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large")
    )


class DeliveryStatusType:
    RECEIVED = "received"
    PROCESSING = "processing"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"

    CHOICES = (
        (RECEIVED, "Received"),
        (PROCESSING, "Processing"),
        (OUT_FOR_DELIVERY, "Out For Delivery"),
        (DELIVERED, "Delivered")
    )
