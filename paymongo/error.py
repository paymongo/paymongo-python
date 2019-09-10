class PaymentRequiredError(Exception):
    """Exception raised for errors in card."""


class AuthenticationError(Exception):
    """Exception raised for errors in authentication."""


class InvalidRequestError(Exception):
    """Invalid parameters were supplied in Paymongo's API."""


class ForbiddenRequestError(Exception):
    """Exception raised when user access forbidden resource."""


class PaymongoError(Exception):
    """Generic Paymongo Error."""
