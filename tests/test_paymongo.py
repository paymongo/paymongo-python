from paymongo import __version__
import paymongo
from paymongo.api_resources import Token, Payment


def test_version():
    assert __version__ == '0.1.0'


def test_use_paymongo_module():
    assert type(paymongo) is not None


def test_initialize_paymongo_token():
    token = paymongo.Token()
    assert isinstance(token, Token) == True


def test_initialize_paymongo_payment():
    payment = paymongo.Payment()
    assert isinstance(payment, Payment) == True
