import paymongo
import faker

fake = faker.Faker()


def test_exec_create_token():
    token = paymongo.Token.create()


def test_create_token():
    """
    Create a token.
    """

    api_key = ''
    profile = fake.simple_profile()
    line1 = profile['address'].split('\n')[0]
    line2 = profile['address'].split('\n')[1]
    city = fake.city()
    state = fake.state()
    postal_code = fake.zipcode()
    country = fake.country()

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
        'email': '',
        'phone': '',
        'name': profile['name']
    }

    data = {
        'number': '4242424242424242',
        'exp_month': 1,
        'exp_year': 22,
        'cvc': '201',
        'billing': billing
    }

    expected_response = {
        "data": {
            "attributes": {
                "number": "4242424242424242",
                "exp_month": 1,
                "exp_year": 22,
                "cvc": "201",
                "billing": {
                    "address": {
                        "line1": line1,
                        "line2": line2,
                        "city": city,
                        "state": state,
                        "postal_code": postal_code,
                        "country": country
                    },
                    "name": billing['name'],
                    "email": "zdoge@doggo.net",
                    "phone": "09171234567"
                }
            }
        }
    }

    token = paymongo.Token.create(data, api_key)

    assert isinstance(token, type(paymongo.Token)) == True
