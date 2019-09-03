import requests

from dotmap import DotMap
from paymongo import api_base

class Token(DotMap):
    """Token response object."""

class TokenService:
    """
    The token object represents a payment source, e.g. your customer's credit cards.
    """

    @classmethod
    def create(cls, card, api_key=None):
        """Creates a one-time use token representing your customer's credit card details."""

        url = api_base + '/v1/tokens'
        response = requests.post(url, json={
            'data': {
                'attributes': card
            }
        }, auth=(api_key, ''))

        if response.status_code not in [200, 201]:
            # Create and raise paymongo exception
            return Token(response.json())

        if  isinstance(response.json(), dict):
            data = response.json().get('data')
            return Token(data)

    @classmethod
    def retrieve(cls, id=None, api_key=None):
        """Retrieve a token given an ID."""

        url  = api_base + '/v1/tokens/' + id
        response = requests.get(url, auth=(api_key, ''))

        if response.status_code not in [200]:
            # Create and raise paymongo exception
            pass

        if  isinstance(response.json(), dict):
            data = response.json().get('data')
            return Token(data)
