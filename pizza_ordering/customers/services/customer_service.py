from ..models import Customer


class CustomerService:
    """
    Customer Service
    """
    model = Customer

    def get_or_create(self, mobile_number, customer_data):
        """
        Customer Get or Create
        :param mobile_number: Mobile number of the customer
        :param customer_data: Customer payload data
        :return: customer, created: Customer object, created or not boolean
        """
        customer, created = self.model.objects.get_or_create(
            mobile_number=mobile_number,
            defaults=customer_data,
        )

        return customer, created
