import requests
from paymongo import api_base

class Token:
    """
    The token object represents a payment source, e.g. your customer's credit cards.
    """

    @classmethod
    def create(cls, data=None, api_key=None):
        """Creates a one-time use token representing your customer's credit card details."""

        url = api_base + '/v1/tokens'
        response = requests.post(url, json={
            'data': {
                'attributes': data
            }
        }, auth=(api_key, ''))

        if response.status_code not in [200, 201]:
            # Create and raise paymongo exception classes
            pass

        return response.json()
