from dotmap import DotMap 

class Payment(DotMap):
    """Payment response object."""

class PaymentService:
    """
    A payment represents a payment transaction that is charged to a specific payment source. 
    """

    @classmethod
    def create(cls, data, api_key=None):
        pass
