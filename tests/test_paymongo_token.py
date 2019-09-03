import faker
import os
import paymongo
import pytest

fake = faker.Faker()


def test_exec_create_token():
    token = paymongo.Token.create(None)


@pytest.fixture
def data():
    profile = fake.simple_profile()
    line1 = profile['address'].split('\n')[0]
    line2 = profile['address'].split('\n')[1]
    city = fake.city()
    state = fake.state()
    postal_code = fake.zipcode()
    country = 'PH'

    address = {
        'line1': line1,
        'line2': line1,
        'city': city,
        'state': state,
        'postal_code': postal_code,
        'country': country
    }

    billing = {
        'address': address,
        'email': profile['mail'],
        'phone': '091712212222',
        'name': profile['name']
    }

    return {
        'number': '4242424242424242',
        'exp_month': 1,
        'exp_year': 22,
        'cvc': '201',
        'billing': billing
    }


def test_create_token(data):
    """
    Create a token.
    """

    api_key = os.getenv('PUBLIC_KEY')
    expected_response = {
        'number': '4242424242424242',
        'exp_month': data['exp_month'],
        'exp_year': data['exp_year'],
        'cvc': data['cvc'],
        'billing': {
            'address': {
                'line1': data['billing']['address']['line1'],
                'line2': data['billing']['address']['line2'],
                'city': data['billing']['address']['city'],
                'state': data['billing']['address']['state'],
                'postal_code': data['billing']['address']['postal_code'],
                'country': data['billing']['address']['country']
            },
            'name': data['billing']['name'],
            'email': data['billing']['email'],
            'phone': data['billing']['phone']
        }
    }

    token = paymongo.Token.create(data, api_key)

    # via dictionary index
    assert token is not None
    token_data_attributes = token.get('attributes')

    assert token.get('id') is not None
    assert token_data_attributes.get('kind') == 'card'

    # via Dot Notation
    assert token.id is not None
    assert token.attributes.billing.name == expected_response['billing'].get(
        'name')


def test_retrieve_token(data):
    """Retrieve token."""

    api_key = os.getenv('PUBLIC_KEY')

    # Create a token.
    create_token = paymongo.Token.create(data, api_key)

    # Retrieve token.
    retrieve_token = paymongo.Token.retrieve(create_token.id, api_key)

    assert create_token.id == retrieve_token.id
    assert create_token.attributes.created == retrieve_token.attributes.created
