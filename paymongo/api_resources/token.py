import requests
import paymongo

from paymongo import api_base, utils
from paymongo.common import Token


class TokenService:
    """
    The token object represents a payment source, e.g. your customer's credit cards.
    """
    @classmethod
    def create(cls, card, api_key=None):
        """Creates a one-time use token representing your customer's credit card details."""

        if not api_key:
            api_key = paymongo.api_key

        url = api_base + '/v1/tokens'
        response = requests.post(url,
                                 json={'data': {
                                     'attributes': card
                                 }},
                                 auth=(api_key, ''))

        if isinstance(response.json(),
                      dict) and response.status_code in [200, 201]:
            data = response.json().get('data')
            return Token(data)

        else:
            utils.handle_exception(response)

    @classmethod
    def retrieve(cls, id=None, api_key=None):
        """Retrieve a token given an ID."""

        if not api_key:
            api_key = paymongo.api_key

        url = api_base + '/v1/tokens/' + id
        response = requests.get(url, auth=(api_key, ''))

        if isinstance(response.json(),
                      dict) and response.status_code in [200, 201]:
            data = response.json().get('data')
            return Token(data)

        else:
            utils.handle_exception(response)
