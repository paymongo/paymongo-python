import os
import pytest


def pytest_runtest_setup(item):
    """
    Fails the tests if key(s) is not set in environment.
    """

    try:
        secret_key = os.environ['SECRET_KEY']
        public_key = os.environ['PUBLIC_KEY']

    except KeyError:
        pytest.exit(
            'No value found for environment variables SECRET_KEY and/or PUBLIC_KEY.')
