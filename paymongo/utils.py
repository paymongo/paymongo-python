from paymongo.error import *


def handle_exception(error):
    exceptions = {
        '400': InvalidRequestError,
        '401': AuthenticationError,
        '402': PaymentRequiredError,
        '403': ForbiddenRequestError
    }

    exception = exceptions.get(str(error.status_code), PaymongoError)

    error = error.json()
    message = error['errors'][0]['detail']
    raise exception(message)
