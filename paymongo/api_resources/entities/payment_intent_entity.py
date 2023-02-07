from paymongo import BaseEntity

class PaymentIntentEntity(BaseEntity):
  def __init__(self, api_resource):
    BaseEntity.__init__(self)

    self.id = api_resource.id
    self.amount = api_resource.attributes['amount']
    self.capture_type = api_resource.attributes['capture_type']
    self.client_key = api_resource.attributes['client_key']
    self.currency = api_resource.attributes['currency']
    self.description = api_resource.attributes['description']
    self.last_payment_error = api_resource.attributes['last_payment_error']
    self.livemode = api_resource.attributes['livemode']
    self.metadata = api_resource.attributes['metadata']
    self.next_action = api_resource.attributes['next_action']
    self.payment_method_allowed = api_resource.attributes['payment_method_allowed']
    self.payment_method_options = api_resource.attributes['payment_method_options']
    self.payments = api_resource.attributes['payments']
    self.setup_future_usage = api_resource.attributes['setup_future_usage']
    self.statement_descriptor = api_resource.attributes['statement_descriptor']
    self.status = api_resource.attributes['status']
    self.created_at = api_resource.attributes['created_at']
    self.updated_at = api_resource.attributes['updated_at']
