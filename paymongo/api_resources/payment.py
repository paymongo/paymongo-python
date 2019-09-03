import requests

from dotmap import DotMap 
from paymongo import api_base

class Payment(DotMap):
    """Payment response object."""

class PaymentService:
    """
    A payment represents a payment transaction that is charged to a specific payment source. 
    """

    @classmethod
    def create(cls, data, api_key=None):
        """
        To charge a payment source, you must create a Payment object.
        """

        url = api_base + '/v1/payments'
        response = requests.post(url, json={
            'data': {
                'attributes': data
            }
        }, auth=(api_key, ''))

        if response.status_code not in [200, 201]:
            # Create and raise paymongo exception
            return Payment(response.json())

        if isinstance(response.json(), dict):
            data = response.json().get('data')
            return Payment(data)
