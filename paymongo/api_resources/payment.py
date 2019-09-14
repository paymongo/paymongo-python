import requests
import paymongo

from paymongo import api_base, utils
from paymongo.common import Payment


class PaymentService:
    """
    A payment represents a payment transaction that is charged to a specific payment source. 
    """
    @classmethod
    def create(cls, data, api_key=None):
        """
        To charge a payment source, you must create a Payment object.
        """
        if not api_key:
            api_key = paymongo.api_key

        url = api_base + '/v1/payments'
        response = requests.post(url,
                                 json={'data': {
                                     'attributes': data
                                 }},
                                 auth=(api_key, ''))

        if isinstance(response.json(),
                      dict) and response.status_code in [200, 201]:
            data = response.json().get('data')
            return Payment(data)

        else:
            utils.handle_exception(response)

    @classmethod
    def retrieve(cls, id, api_key=None):
        """
        You can retrieve a Payment by providing a payment ID.
        """

        if not api_key:
            api_key = paymongo.api_key

        url = api_base + '/v1/payments/' + id
        response = requests.get(url, auth=(api_key, ''))

        if isinstance(response.json(),
                      dict) and response.status_code in [200, 201]:
            data = response.json().get('data')
            return Payment(data)

        else:
            utils.handle_exception(response)
