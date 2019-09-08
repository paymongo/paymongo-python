import paymongo
import os

from paymongo import __version__
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

def test_allow_global_setting_of_api_key():
    paymongo.api_key = os.getenv('SECRET_KEY')
    assert paymongo.api_key is not None
