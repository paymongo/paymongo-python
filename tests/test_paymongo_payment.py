import os
import paymongo


def test_exec_create_payment():
    token = paymongo.Payment.create(None)


def test_create_payment():
    """
    Create a payment.
    """

    pk = os.getenv('PUBLIC_KEY')
    sk = os.getenv('SECRET_KEY')
    token = paymongo.Token.create(card={
        'number': '4242424242424242',
        'exp_month': 12,
        'exp_year': 22,
        'cvc': '212'
    },
                                  api_key=pk)

    source = {'id': token.id, 'type': 'token'}

    data = {
        'amount': 10000,
        'currency': 'PHP',
        'description': '',
        'statement_descriptor': '',
        'source': source
    }

    payment = paymongo.Payment.create(data, sk)

    assert payment.type == 'payment'
    assert payment.id is not None
    assert payment.attributes.amount == data['amount']
    assert payment.attributes.fee is not None
    assert payment.relationships.source.data == source
