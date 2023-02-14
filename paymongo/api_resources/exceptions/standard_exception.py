from paymongo import PaymongoError

class StandardException(Exception):
  def __init__(self, response):
    self.data = response
    self.errors = list(map(lambda error: PaymongoError(error=error), response['errors']))
