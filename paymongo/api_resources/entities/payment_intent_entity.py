from paymongo import BaseEntity

class PaymentIntentEntity(BaseEntity):
  def __init__(self, resource):
    BaseEntity.__init__(self)

    data = resource['data']
    attributes = data['attributes']

    self.id = data['id']
    self.amount = attributes['amount']
    self.capture_type = attributes['capture_type']
    self.client_key = attributes['client_key']
    self.currency = attributes['currency']
    self.description = attributes['description']
    self.livemode = attributes['livemode']
    self.statement_descriptor = attributes['statement_descriptor']
    self.status = attributes['status']
    self.last_payment_error = attributes['last_payment_error']
    self.payment_method_allowed = attributes['payment_method_allowed']
    self.payments = attributes['payments']
    self.next_action = attributes['next_action']
    self.payment_method_options = attributes['payment_method_options']
    self.metadata = attributes['metadata']
    self.setup_future_usage = attributes['setup_future_usage']
    self.created_at = attributes['created_at']
    self.updated_at = attributes['updated_at']