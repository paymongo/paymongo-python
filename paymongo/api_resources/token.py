class Token:
    """
    The token object represents a payment source, e.g. your customer's credit cards.
    """

    def __init__(self, number=None, exp_month=None, exp_year=None, cvc=None, billing=None):
        self.number = number
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.cvc = cvc
        self.billing = billing

    @classmethod
    def create(cls, data=None, api_key=None):
        """Creates a one-time use token representing your customer's credit card details."""
        return cls
