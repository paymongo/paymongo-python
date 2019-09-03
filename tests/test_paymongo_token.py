import paymongo
import faker
import os

fake = faker.Faker()


def test_exec_create_token():
    token = paymongo.Token.create()


def test_create_token():
    """
    Create a token.
    """

    api_key = os.getenv('API_KEY')
    profile = fake.simple_profile()
    line1 = profile['address'].split('\n')[0]
    line2 = profile['address'].split('\n')[1]
    city = fake.city()
    state = fake.state()
    postal_code = fake.zipcode()
    country = fake.country

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

    data = {
        'number': '4242424242424242',
        'exp_month': 1,
        'exp_year': 22,
        'cvc': '201'
    }

    expected_response_data = {
        'number': '4242424242424242',
        'exp_month': data['exp_month'],
        'exp_year': data['exp_year'],
        'cvc': data['cvc'],
        'billing': {
            'address': {
                'line1': line1,
                'line2': line2,
                'city': city,
                'state': state,
                'postal_code': postal_code,
                'country': country
            },
            'name': billing['name'],
            'email': billing['email'],
            'phone': billing['phone']
        }
    }

    token = paymongo.Token.create(data, api_key)

    assert token is not None

    assert token.get('data').get('id') is not None
    assert token.get('data').get('attributes').get('kind') == 'card'
