import os
import paymongo
import pytest


def test_exec_create_payment():
    token = paymongo.Payment.create(None)


@pytest.fixture
def token():
    pk = os.getenv('PUBLIC_KEY')
    return paymongo.Token.create(card={
        'number': '4242424242424242',
        'exp_month': 12,
        'exp_year': 22,
        'cvc': '212'
    },
                                 api_key=pk)


@pytest.fixture
def payment(token):
    sk = os.getenv('SECRET_KEY')
    source = {'id': token.id, 'type': 'token'}
    data = {
        'amount': 10000,
        'currency': 'PHP',
        'description': '',
        'statement_descriptor': '',
        'source': source
    }

    return paymongo.Payment.create(data, sk)


def test_create_payment(token):
    """
    Create a payment.
    """

    sk = os.getenv('SECRET_KEY')
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


def test_retrieve_payment(payment):
    """
    Retrieve a payment by id.
    """
    sk = os.getenv('SECRET_KEY')
    retrieved_payment = paymongo.Payment.retrieve(payment.id, sk)

    assert isinstance(payment.id, str) == True
    assert retrieved_payment.id == payment.id
    assert retrieved_payment.attributes.amount == payment.attributes.amount
    assert retrieved_payment.attributes.fee is not None
    assert retrieved_payment.relationships.source == payment.relationships.source